# Idea OS System Design

## Objective

The system converts raw brainstorming into a measurable research pipeline:

```text
RAW IDEAS -> NORMALIZED PROBLEMS -> 100-POINT MATURITY -> MERGE CANDIDATES -> CLUSTERS -> RESEARCH CANDIDATES -> BRIEFS
```

The durable unit is a YAML idea record. Scripts compute maturity, links, merge
scores, clusters, research candidates, briefs, indexes, and short planning
bridge notes from that record.

## Architecture

| Layer | Files | Responsibility |
| --- | --- | --- |
| Data | `ideas/**/*.yaml` | Canonical idea records |
| Schema | `schemas/*.yaml`, `idea_os/models.py` | Required fields, statuses, maturity rules |
| Core | `idea_os/` | YAML I/O, store, normalization, scoring, merge logic, clustering, research, planning sync |
| CLI | `scripts/*.py` | Automation-ready command entrypoints |
| Outputs | `clusters/`, `research/`, `index/`, `graph/` | Generated artifacts |
| Bridge | planning scripts | Short planning integration |

## Data Flow

1. `new_idea.py` creates a low-maturity idea in `ideas/raw/`.
2. `normalize_problem.py` writes the Given/optimize/constraints structure.
3. `score_maturity.py` calculates the 100-point maturity score and level.
4. `detect_merge_candidates.py` compares ideas and recommends merge actions.
5. `generate_clusters.py` groups ideas with merge score at least 60/100.
6. `generate_research_candidates.py` promotes clusters that pass readiness gates.
7. `generate_research_brief.py` writes Markdown briefs for candidate review.
8. `generate_index.py` rebuilds idea, cluster, and research indexes.

## Decision Boundary

All automated decisions use `maturity_score`, `maturity_level`, merge scores, or
research readiness scores. The retired compact score is not a decision input.
`status` remains an operational lifecycle marker; `executing` and `archived`
are terminal workflow states.
