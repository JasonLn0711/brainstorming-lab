# Research Pipeline

## Idea To Research

Research candidates are generated from clusters, not isolated excitement.

`research/generate_candidates.py` selects a cluster when:

- cluster size is at least 2
- average score is at least 12
- at least one idea has `maturity.testability >= 3`

## Why Clusters Matter

A cluster suggests that several ideas share a reusable problem shape. That is a
better research signal than a single attractive note.

## Paper Or Project Flow

1. Build or update YAML ideas.
2. Score them.
3. Generate graph and clusters.
4. Generate research candidates.
5. If a candidate becomes real, write a graduation packet.
6. Move execution into a standalone repo.
7. Keep only locator/status notes in planning.

## Claim Boundary

Research-ready means suitable for a bounded research design or experiment. It
does not mean validated, deployed, clinically safe, legally confirmed, or ready
for production.
