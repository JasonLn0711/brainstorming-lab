"""Generate a review draft only after the complete Opus transcription exists."""
from pathlib import Path
import csv
import hashlib
import json

p = Path(__file__).resolve().parent

def stamp(seconds):
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'

def revise(text, rules):
    changes = []
    for old, new, source in rules:
        if old in text:
            text = text.replace(old, new)
            changes.append((old, new, source))
    return text, changes

assert stamp(3661.234) == '01:01:01,234'
assert revise('沈柏楊說三規一章', [('沈柏楊', '沈伯洋', 'S01')])[0] == '沈伯洋說三規一章'
assert revise('原話 1.4 倍', [('不相關', '替換', 'context')]) == ('原話 1.4 倍', [])

if __name__ == '__main__':
    receipt_path = p / 'best_transcription_receipt.json'
    if not receipt_path.exists():
        raise SystemExit('Complete ASR receipt is missing; partial input will not be published as a full transcript.')
    receipt = json.loads(receipt_path.read_text())
    assert receipt['execution_status'] == 'LIVE_FULL_COMPLETED'
    assert hashlib.sha256((p / 'source_best.webm').read_bytes()).hexdigest() == receipt['source_sha256']
    rows = [json.loads(line) for line in (p / 'best_segments.jsonl').read_text().splitlines()]
    assert len(rows) == receipt['segments']
    assert all(0 <= r['start'] <= r['end'] <= receipt['duration'] + 1 for r in rows)
    assert all(r['start'] >= rows[i-1]['end'] - .1 for i, r in enumerate(rows) if i)
    config = json.loads((p / 'correction_rules.json').read_text())
    corrected, changes, flags = [], [], []
    review_path = p / 'best_reviewed_overrides.json'
    overrides = json.loads(review_path.read_text()) if review_path.exists() else {}
    for number, row in enumerate(rows, 1):
        text, edits = revise(row['text'].strip(), config['rules'])
        override = overrides.get(str(number), {})
        assert not override or override['original_text'] == row['text'], 'Override belongs to different input.'
        text = override.get('text', text)
        start, end = override.get('start', row['start']), override.get('end', row['end'])
        corrected.append(dict(segment=number, start=start, end=end, text=text))
        for old, new, source in edits:
            changes.append(dict(segment=number, start=row['start'], end=row['end'], old=old, new=new, source_id=source, source=config['sources'][source]))
        reasons = []
        if row['end'] - row['start'] > 30:
            reasons.append('duration_over_30s')
        if row['avg_logprob'] < -1:
            reasons.append('low_log_probability')
        if row['compression_ratio'] > 2.4:
            reasons.append('high_compression_ratio')
        if number > 1 and text == corrected[-2]['text']:
            reasons.append('adjacent_exact_repeat')
        if reasons:
            flags.append(dict(segment=number, start=row['start'], end=row['end'], text=text, reasons=reasons))
    assert len(corrected) == len(rows)
    assert all(0 <= r['start'] <= r['end'] <= receipt['duration'] + 1 for r in corrected)
    assert all(r['start'] >= corrected[i-1]['end'] - .1 for i, r in enumerate(corrected) if i)
    # shortcut: lexical rules create a review draft; ambiguous speech still requires contextual review.
    (p / 'best_transcript_corrected_draft.txt').write_text(''.join(r['text']+'\n' for r in corrected))
    (p / 'best_transcript_corrected_draft.srt').write_text(''.join(f"{r['segment']}\n{stamp(r['start'])} --> {stamp(r['end'])}\n{r['text']}\n\n" for r in corrected))
    (p / 'best_segments_corrected_draft.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in corrected))
    with (p / 'best_correction_log.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['segment','start','end','old','new','source_id','source'])
        writer.writeheader()
        writer.writerows(changes)
    (p / 'best_quality_review.json').write_text(json.dumps(flags, ensure_ascii=False, indent=2)+'\n')
    result = dict(status='draft_requires_full_review', segments=len(rows), replacement_events=len(changes), flagged_segments=len(flags), original_preserved=True, full_audio_listening=False, web_fact_check='in_progress', reviewed_overrides=len(overrides), timing_changes=sum('start' in v or 'end' in v for v in overrides.values()))
    (p / 'best_correction_receipt.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result))
