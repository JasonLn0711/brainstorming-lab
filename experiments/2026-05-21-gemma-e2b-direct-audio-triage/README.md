# Gemma E2B Direct-Audio Triage Experiment

## First Principle

The scarce resource is safe understanding of short patient symptom answers under noisy
audio and limited clinician attention.

The bottleneck hypothesis is that traditional ASR can transform an utterance into
semantically unrelated text before retrieval or question routing sees the real signal.
The bold experimental move is to let Gemma 4 E2B listen directly and emit bounded
structured intake fields, then compare that path against ASR-driven and hybrid paths.

This experiment does not prove clinical deployment readiness, does not use real patient
data, and does not remove staff review.

## Research Question

Can Gemma 4 E2B direct audio-to-structured-intake reduce ASR-induced semantic drift
without increasing silent clinical over-correction, missed high-risk triggers, invalid
JSON, or latency?

## Experiment Arms

| Arm | Pipeline | Purpose |
| --- | --- | --- |
| A | ASR transcript -> embedding / retrieval -> structured intake | Current baseline. |
| B | ASR transcript -> text LLM repair -> retrieval / structured intake | Measures whether text repair can recover from bad transcripts. |
| C | Gemma 4 E2B audio -> structured intake | Bold replacement hypothesis. |
| D | Gemma 4 E2B audio + ASR transcript disagreement gate | Safety comparator and likely production fallback. |

## Fixture Design

Use only synthetic, scripted, or explicitly consented non-patient clips.

Minimum first pass:

- 30 to 50 short clips.
- Each clip is 30 seconds or shorter.
- Each case has a ground-truth `case_id`, intended symptom, expected structured fields,
  expected next question, and expected safety decision.
- Include clean audio, noise, non-native English accent, code-switching, vague answers,
  negation, near-homophones, and irrelevant patient statements.

Required symptom families:

- Dysuria / burning urination.
- Chest pain.
- Shortness of breath.
- Dizziness.
- Fever.
- Cough.
- Abdominal pain.
- Palpitations.
- Low SpO2 context.
- Vague discomfort.

## Prompt Contract

Audio should be placed before the text prompt when the runtime supports that ordering.
The prompt must require JSON only and must reject diagnosis, final triage level, treatment
advice, or clinical certainty claims.

Required output shape:

```json
{
  "model_understood_transcript": "",
  "primary_symptom_candidate": "",
  "symptom_candidates": [
    {
      "symptom": "",
      "confidence": 0.0,
      "evidence_from_audio": "",
      "risk_if_wrong": "low|medium|high"
    }
  ],
  "structured_fields": {
    "chief_complaint": "",
    "duration": "",
    "severity": "",
    "red_flags": [],
    "negated_symptoms": []
  },
  "decision": "accept|ask_clarification|staff_review",
  "next_question": "",
  "uncertainty_reason": "",
  "safety_boundary": "not_diagnosis_not_final_triage"
}
```

## Run Log

Each inference run should append one JSONL record with:

- `run_id`
- `timestamp`
- `case_id`
- `arm`
- `audio_sha256`
- `audio_duration_seconds`
- `sample_rate_hz`
- `channels`
- `noise_condition`
- `speaker_condition`
- `prompt_version`
- `schema_version`
- `model_id`
- `model_revision`
- `runtime`
- `quantization`
- `temperature`
- `top_p`
- `top_k`
- `seed`
- `raw_output`
- `parsed_output`
- `json_valid`
- `schema_valid`
- `schema_error`
- `latency_audio_load_ms`
- `latency_inference_ms`
- `latency_parse_ms`
- `latency_total_ms`
- `error_type`

## Evaluation Log

Each evaluated case should append one JSONL record with:

- `run_id`
- `case_id`
- `arm`
- `gold_symptom`
- `predicted_symptom`
- `symptom_top1_correct`
- `symptom_top3_correct`
- `next_question_correct`
- `decision_correct`
- `negation_correct`
- `high_risk_trigger_correct`
- `unsafe_silent_correction`
- `hallucinated_symptom`
- `missed_clarification`
- `unnecessary_clarification`
- `staff_review_should_trigger`
- `staff_review_triggered`
- `reviewer_notes`

## Metrics

Primary metrics:

- Symptom top-1 accuracy.
- Symptom top-3 accuracy.
- Unsafe silent-correction rate.
- Dangerous miss rate.
- Negation handling accuracy.
- Clarification-needed detection rate.
- JSON-valid and schema-valid rate.
- p50 and p95 latency.

Secondary metrics:

- Unnecessary clarification rate.
- Staff-review trigger precision and recall.
- Direct-audio win rate against ASR-only on semantic-drift cases.
- Audit quality of `model_understood_transcript`.

## Promotion Rule

Gemma direct audio can become the primary demo interpreter only if it improves
symptom-level accuracy and semantic-drift recovery while keeping unsafe silent correction,
high-risk misses, invalid JSON, and latency below preset thresholds.

## Kill Or Revise Rule

If direct audio confidently invents clinical meaning, misses negation, or suppresses
uncertainty instead of asking confirmation, keep Gemma as a verifier only and do not
replace ASR.

## Planning Boundary

Planning receives only the experiment status, canonical packet path, next test, and
capacity note. Full prompts, fixtures, logs, raw audio, and model outputs stay outside
planning.
