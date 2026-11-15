from pathlib import Path
from dataclasses import asdict
import json
from faster_whisper import WhisperModel
from faster_whisper.audio import decode_audio

p = Path(__file__).resolve().parent
rows = [json.loads(s) for s in (p / 'segments.jsonl').read_text().splitlines()]
duration = json.loads((p / 'transcription_receipt.json').read_text())['duration']
intervals = []
for i, s in enumerate(rows):
    repeated = i >= 2 and s['text'] == rows[i-1]['text'] == rows[i-2]['text']
    if s['avg_logprob'] < -1 or s['compression_ratio'] > 2.4 or repeated:
        intervals.append((max(0, s['start'] - 2), min(duration, s['end'] + 2)))
    prior = rows[i-1]['end'] if i else 0
    if s['start'] - prior > 30:
        intervals.append((prior, s['start']))
if duration - rows[-1]['end'] > 30:
    intervals.append((rows[-1]['end'], duration))
merged = []
for start, end in sorted(intervals):
    if merged and start <= merged[-1][1] + 2:
        merged[-1][1] = max(end, merged[-1][1])
    else:
        merged.append([start, end])
assert all(0 <= a < b <= duration for a, b in merged)
(p / 'audio_review_ranges.json').write_text(json.dumps(merged, indent=2) + '\n')
model_path = '/home/jnclaw/.cache/huggingface/hub/models--SoybeanMilk--faster-whisper-Breeze-ASR-25/snapshots/85be11de5f67aaa6a92e931622f1c2b55cc1dd3a'
model = WhisperModel(model_path, device='cuda', compute_type='int8')
audio = decode_audio(str(p / 'source.m4a'), sampling_rate=16000)
with (p / 'audio_review_candidates.jsonl').open('w') as out:
    for n, (start, end) in enumerate(merged, 1):
        segments, _ = model.transcribe(audio[round(start*16000):round(end*16000)], language='zh', beam_size=5, vad_filter=True, condition_on_previous_text=False)
        candidates = []
        for segment in segments:
            row = asdict(segment)
            row['start'] += start
            row['end'] += start
            candidates.append(row)
        out.write(json.dumps(dict(range_id=n, start=start, end=end, candidates=candidates), ensure_ascii=False) + '\n')
        out.flush()
        print(f'{n}/{len(merged)} ranges reviewed; {start:.2f}-{end:.2f}', flush=True)
(p / 'audio_review_receipt.json').write_text(json.dumps(dict(model=model_path, ranges=len(merged), status='completed', purpose='correction_candidates_only', human_listening=False), indent=2)+'\n')
