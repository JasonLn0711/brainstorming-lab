# Project Graduation: Provenance Attends To Evidence

Date: 2026-06-01
Source idea: `idea_000044`
Target repo: `../paper-3-provenance-attends-to-evidence`
State: executing / paper-incubation

## Why This Is Real Now

The research line has moved from broad `Knowledge Graph Compression + SLM` brainstorming into a narrowed paper object: provenance-bounded evidence graph packets for stable small-model decision support. The expert review converged on a first-paper claim that is testable with public datasets, hard baselines, ablations, and evidence-discipline metrics.

The standalone repo exists so the paper can advance as a reproducible Q1-oriented research project instead of remaining a long-running brainstorm.

## First Output

The first execution output is `PB-EGP-50`: a 40-50 record pilot built from public claim/evidence datasets with packet schema v0, gold lineage fields, baseline contexts, model-output schema, and human-audit rubric.

## User / Audience / Owner

Primary audience: expert reviewers, future coauthors, and Q1 journal reviewers evaluating whether the method defines a distinct scientific object beyond GraphRAG, KGQA, graph summarization, or prompt compression.

Owner: `paper-3-provenance-attends-to-evidence`. `brainstorming-lab` keeps source reasoning, expert packets, Idea OS links, and graduation rationale.

## Scope

In:
- public-data pilot from SciFact plus FEVEROUS / SciTab-style structured evidence;
- provenance-bounded packet schema;
- constrained evidence-preservation objective;
- top-k text, generic summary, flat evidence list, context compression, uncompressed graph, and graph-pruning baselines;
- unsupported-claim rate, provenance / citation validity, decision correctness, and non-evidential decision stability;
- human audit with atomic-claim support labels.

Out for the first paper:
- generic GraphRAG product development;
- private meeting / medical / scam data as primary evidence;
- dynamic pheromone routing;
- ancient-script symbolic testbeds;
- clinical, legal, or security deployment claims.

## Evidence

- Expert review packet: `expert-review-packets/2026-06-01-kg-compression-slm/`.
- Final narrowed plan: `expert-review-packets/2026-06-01-kg-compression-slm/12_narrowed_pilot_plan.md`.
- Idea OS record: `ideas/structured/idea_000044_provenance_bounded_graph_packets_for_slm_decision_support.yaml`.
- New execution repo: `../paper-3-provenance-attends-to-evidence`.
- Execution repo scaffold test passed with `uvx --with pytest pytest`.

## First Repo Structure

```text
paper-3-provenance-attends-to-evidence/
  README.md
  AGENTS.md
  docs/
  schemas/
  experiments/
  src/pb_egp/
  tests/
```

## Planning Bridge Update

- Project locator: `../planning-everything-track/data/projects/2026-06-provenance-attends-to-evidence.md`.
- Day-note bridge: `../planning-everything-track/weeks/2026-W23/days/2026-06-01.md`.
- Capacity impact: paper incubation is active but bounded; W23 does not open a broad experiment sprint while WISA, CDE, coursework, and June 7 deadlines remain active.
- Next action: freeze schema v0 and create the `PB-EGP-50` record manifest after the early-June fixed academic cluster is safe.
- Review date: 2026-06-08.

## Move Checklist

- [x] Create standalone repo.
- [x] Move copied expert packet and source notes into the standalone repo.
- [x] Add execution README, AGENTS, schemas, pilot plan, metrics, baselines, audit rubric, and tests.
- [x] Add planning locator/status.
- [x] Keep full brainstorming detail in `brainstorming-lab`.
- [ ] Build `PB-EGP-50` record manifest.
- [ ] Run first baseline/model pilot.
