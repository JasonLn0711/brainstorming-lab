# Calibration Papers

Calibration papers keep the scientific-quality score from drifting.

Before trusting repeated AI or human scores under
`scientific_paper_evaluation_v1`, build a small gold-score set:

| Slot | Purpose |
| --- | --- |
| `01_strong_paper/` | High-quality paper with strong problem, method, evidence, honesty, and reproducibility. |
| `02_solid_paper/` | Good paper with normal limitations. |
| `03_overclaim_paper/` | Interesting paper where claims exceed evidence. |
| `04_bad_baseline_paper/` | Paper with weak or unfair baselines. |
| `05_reproducibility_strong_paper/` | Paper with unusually strong code, data, environment, and protocol support. |
| `06_reproducibility_weak_paper/` | Paper where reproduction is hard or under-specified. |

Each calibration folder should eventually contain:

```text
gold_score.md
scientific_evaluation.yaml
claim_evidence_matrix.md
disagreement_note.md
```

Do not add copyrighted PDFs unless the repo has a clear local-only policy for
that source. Prefer citation links, short notes, and reproducible score records.
