from pathlib import Path
import json
import hashlib
from faster_whisper import WhisperModel

folder = Path(__file__).resolve().parent
model_path = Path('/home/jnclaw/.cache/huggingface/hub/models--SoybeanMilk--faster-whisper-Breeze-ASR-25/snapshots/85be11de5f67aaa6a92e931622f1c2b55cc1dd3a')
def stamp(seconds):
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'
assert stamp(3661.234) == '01:01:01,234'
print('Loading Breeze-ASR-25', flush=True)
model = WhisperModel(str(model_path), device='cuda', compute_type='int8')
segments, info = model.transcribe(str(folder / 'source_best.webm'), language='zh', beam_size=5, vad_filter=True, condition_on_previous_text=False, initial_prompt='以下是繁體中文逐字稿。')
count = 0
last = 0
with (folder / 'best_transcript.txt').open('w') as txt, (folder / 'best_transcript.srt').open('w') as srt, (folder / 'best_segments.jsonl').open('w') as raw:
    for count, segment in enumerate(segments, 1):
        assert 0 <= segment.start <= segment.end <= info.duration + 1
        assert segment.start >= last - 0.1
        last = segment.end
        text = segment.text.strip()
        txt.write(text + '\n'); txt.flush()
        srt.write(f'{count}\n{stamp(segment.start)} --> {stamp(segment.end)}\n{text}\n\n'); srt.flush()
        raw.write(json.dumps(segment._asdict(), ensure_ascii=False) + '\n'); raw.flush()
        if count % 100 == 0:
            print(f'{count} segments; audio position {stamp(last)}', flush=True)
assert count > 0 and (folder / 'best_transcript.txt').stat().st_size > 0
receipt = dict(model='SoybeanMilk/faster-whisper-Breeze-ASR-25', revision=model_path.name, device='cuda', compute_type='int8', condition_on_previous_text=False, beam_size=5, vad_filter=True, language=info.language, duration=info.duration, segments=count, last_segment_end=last, source_sha256=hashlib.sha256((folder / 'source_best.webm').read_bytes()).hexdigest(), execution_status='LIVE_FULL_COMPLETED', runtime_validity='valid_target_runtime', validation_mode='availability_validation', accuracy='not_evaluated', latency='not_evaluated')
(folder / 'best_transcription_receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print('Completed', flush=True)
