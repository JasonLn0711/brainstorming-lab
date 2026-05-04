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

## Claim Boundary

Research-ready means suitable for a bounded research design or experiment. It
does not mean validated, deployed, clinically safe, legally confirmed, or ready
for production.
