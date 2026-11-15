# Weekly Paper Lab Agent Contract

Read before selecting, scoring, recording or reviewing a weekly paper. Paths
below are relative to the repo root. This contract preserves the paper-lab
requirements formerly loaded in AGENTS.md; it does not activate model runs.

## Weekly Paper Lab Rules

- Treat `weekly-paper-lab/` as the doctoral-training input layer for Idea OS.
- Use `weekly-paper-lab/shortlists/<YYYY-Www>.yaml` to record 3 to 5 candidate papers before creating the selected paper folder.
- Shortlist scoring must be evidence-driven: raw observable evidence, fixed rubric rules, recomputed score.
- A score is invalid unless every subscore is backed by observable evidence; missing or unknown evidence counts as false and contributes 0.
- Previously selected papers or essays are excluded from new shortlists by normalized `paper_id`, title, or identity URL. Revisit work belongs in the original paper folder or an Idea OS update, not as a new weekly pick.
- Each selected paper gets one folder under `weekly-paper-lab/papers/<YYYY-Www>-<slug>/`.
- `paper.yaml` is canonical for paper status, triage score, reproduction level, artifact path, links, and planning sync.
- Selected papers must include `idea_connections` with objective 100-point `paper_connection_rubric_v2` scores before reading or implementation starts.
- `paper_connection_rubric_v2` evidence list fields must contain the actual observed items; do not replace them with bare counts.
- Selected papers must include `synthesis_assessment` with objective `paper_synthesis_rubric_v1` scores to decide whether the paper can combine with existing ideas into a future research method or reference.
- Keep the Markdown files as the human lab notebook: metadata, problem, method, figures, RTX 5080 log, bottlenecks, research seed, selection/connection scoring report, and scientific evaluation report.
- Every selected paper must include `07_scoring_report.md` explaining why the shortlist, connection, and synthesis scores were assigned; unknown evidence must be named instead of guessed.
- Every selected paper must include `scientific_evaluation.yaml` and `08_scientific_evaluation.md` for post-reading paper quality evaluation under `scientific_paper_evaluation_v1`.
- Scientific quality scoring is separate from shortlist triage: triage decides whether to read the paper; scientific evaluation decides whether the paper's problem, method, evidence, claims, limits, and reproducibility are strong.
- Scientific evaluation coefficients are limited to `0`, `0.25`, `0.5`, `0.75`, or `1`; every subscore must have an evidence note, and validator-recomputed penalties/caps/confidence/risk fields must match the YAML.
- Use the three-week cycle: `main_a`, `main_b`, then `cross_domain`.
- Use `scripts/check_paper_shortlist.py` before selecting the weekly paper and `scripts/check_paper_lab.py` plus `scripts/check_paper_quality.py` before weekly review or planning sync when paper folders changed.
- Weekly Paper Lab must stay coupled to `planning-everything-track`: update the current day note when a paper is selected or run, update the weekly plan with the scheduled reading/run block and next test, and keep planning notes short.
- Keep large models, datasets, checkpoints, caches, credentials, sensitive evidence, and generated run artifacts out of git.
- If a paper produces a real research question, create or update an Idea OS YAML record and link back to the paper folder.
- Planning receives only title, paper ID, status, next test, canonical path, linked idea IDs, and capacity note.

