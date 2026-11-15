from pathlib import Path
from dataclasses import asdict
import json
from faster_whisper import WhisperModel
from faster_whisper.audio import decode_audio

p = Path(__file__).resolve().parent
clips = [(2086, 7483, 7498), (2136, 7617, 7630), (2274, 7963, 7980), (2893, 9856, 9869), (3084, 10616, 10630), (3085, 10619, 10632), (3138, 10759, 10773)]
assert all(a < b for _, a, b in clips)
assert (p/'best_transcription_receipt.json').exists(), 'Wait for full primary ASR before review.'
model = WhisperModel('/home/jnclaw/.cache/huggingface/hub/models--SoybeanMilk--faster-whisper-Breeze-ASR-25/snapshots/85be11de5f67aaa6a92e931622f1c2b55cc1dd3a', device='cuda', compute_type='int8')
audio = decode_audio(str(p/'source_best.webm'),sampling_rate=16000)
with (p/'best_lexical_review_4.jsonl').open('w') as out:
    for original_segment, start, end in clips:
        segments, _ = model.transcribe(audio[start*16000:end*16000],language='zh',beam_size=5,vad_filter=False,condition_on_previous_text=False,word_timestamps=True)
        rows=[]
        for s in segments:
            r=asdict(s)
            r['start']+=start
            r['end']+=start
            for word in r['words']:
                word['start']+=start
                word['end']+=start
            rows.append(r)
        out.write(json.dumps(dict(original_segment=original_segment,clip_start=start,clip_end=end,segments=rows),ensure_ascii=False)+'\n')
        out.flush()
        print(original_segment,[(r['start'],r['end'],r['text']) for r in rows],flush=True)
