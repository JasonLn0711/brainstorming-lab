# Idea OS System Design

## Objective

The system converts raw brainstorming into a closed loop:

```text
RAW IDEAS -> STRUCTURED IDEAS -> CLUSTERS -> RESEARCH -> EXECUTION -> FEEDBACK -> IMPROVED IDEAS
```

The durable unit is a YAML idea record. The scripts compute score, links,
clusters, graph edges, research candidates, and planning bridge notes from that
record.

## Architecture

| Layer | Files | Responsibility |
| --- | --- | --- |
| Data | `ideas/**/*.yaml` | Canonical idea records |
| Schema | `schemas/*.yaml`, `idea_os/models.py` | Required fields, statuses, score rules |
| Core | `idea_os/` | YAML I/O, store, scoring, adaptive selection, similarity, graphing, clustering, research, planning sync |
| CLI | `scripts/*.py`, `graph/build_graph.py`, `clustering/auto_cluster.py`, `research/generate_candidates.py` | Automation-ready command entrypoints |
| Outputs | `graph/`, `clustering/`, `research/`, `index/` | Generated artifacts |
| Bridge | `scripts/push_to_planning.py`, `scripts/suggest_today_ideas.py`, `scripts/pull_feedback.py` | Short planning integration |

## Data Flow

1. `new_idea.py` creates a low-maturity idea in `ideas/raw/`.
2. `score_idea.py` calculates maturity and moves the file to the matching folder.
3. `link_ideas.py`, shared tags, and similarity form the graph.
4. `auto_cluster.py` groups related ideas.
5. `generate_candidates.py` selects mature clusters for research.
6. `weekly_review.py` selects ideas with exploitation, novelty exploration, and controlled randomness.
7. Planning scripts write only bridge notes and daily suggestions.
8. `pull_feedback.py` consumes explicit feedback markers and updates ideas.

## Adaptive Selection

Weekly selection reads only `ideas/structured/` and `ideas/evolving/`.

The selector computes impact, feasibility, maturity, novelty, execution cost,
and priority-tag alignment. It writes `selection_score` separately from the idea
maturity `score`.

Adaptive epsilon is bounded by config. Incomplete or overloaded prior-week
reviews increase exploration; high-success reviews reduce it.

## Boundaries

`brainstorming-lab` owns the idea database and detailed thinking.
`planning-everything-track` owns priority, capacity, commitments, and short
status links. Execution belongs in standalone project repos after graduation.
