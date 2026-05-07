# Research Pipeline

Research candidates are generated from clusters, not isolated excitement.

The pipeline is:

```bash
python3 scripts/normalize_problem.py
python3 scripts/score_maturity.py
python3 scripts/detect_merge_candidates.py
python3 scripts/generate_clusters.py
python3 scripts/generate_research_candidates.py
python3 scripts/generate_research_brief.py
python3 scripts/generate_index.py
```

## Cluster To Research

`generate_research_candidates.py` promotes a cluster only when it has at least
two ideas, average maturity at least 65/100, strong testability, enough evidence,
feasibility, a normalized problem, baselines, and metrics.

## Why Clusters Matter

A cluster suggests that several ideas share a reusable problem shape. That is a
better research signal than one attractive note.

## Paper Or Project Flow

1. Build or update YAML ideas.
2. Normalize and score them.
3. Detect merge candidates and clusters.
4. Generate research candidates and briefs.
5. If a candidate becomes real, write a graduation packet.
6. Move execution into a standalone repo.
7. Keep only locator/status notes in planning.

## Weekly Paper Lab Input

`weekly-paper-lab/` feeds the research pipeline without replacing Idea OS.
Paper folders keep reading notes, method breakdowns, RTX 5080 minimum
experiments, failure logs, scoring reports, and research-question seeds. The
scoring report explains why the evidence fields were assigned before the
validator recomputes the numbers.

After reading, `scientific_evaluation.yaml` and
`08_scientific_evaluation.md` score the paper's scientific quality under
`scientific_paper_evaluation_v1`. This is not the same as shortlist triage:
triage answers "should we read this paper this week"; scientific evaluation
answers "how strong are the paper's problem, method, evidence, claims,
limitations, and reproducibility." Every subscore must have an evidence note,
and the validator recomputes raw score, penalties, caps, confidence score, and
risk gates.

When a paper creates a real research
direction, create or update an Idea OS YAML record and link back to the paper
folder through `source`, `evidence`, `connections`, or `next_steps`.

Run this before weekly review when paper folders changed:

```bash
python3 scripts/check_paper_shortlist.py
python3 scripts/check_paper_lab.py
python3 scripts/check_paper_quality.py
```

After those checks pass, update the planning control plane with the paper title,
status, scheduled reading/run block, next test, canonical paper path, linked
Idea OS IDs, and capacity note. Do not copy detailed paper notes or artifact
contents into planning.

## Claim Boundary

Research-ready means suitable for a bounded research design or experiment. It
does not mean validated, deployed, clinically safe, legally confirmed, or ready
for production.
