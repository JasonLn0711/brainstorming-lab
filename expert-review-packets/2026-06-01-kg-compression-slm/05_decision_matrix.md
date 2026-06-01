# Decision Matrix

## Candidate Scoring

Scores are initial internal estimates for expert discussion, not final evidence.

| Direction | Novelty | Feasibility | Evaluation Clarity | Fit To Existing Repo Strengths | Risk | Recommended Role |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Provenance-preserving KG compression | 5 | 4 | 5 | 5 | 2 | First paper candidate |
| Pheromone-based dynamic KG compression | 4 | 3 | 3 | 4 | 3 | Method extension or second paper |
| Latent-state KG compression | 5 | 3 | 4 | 5 | 3 | First paper if domain is clean |
| Low-resource symbolic KG compression | 5 | 2 | 3 | 3 | 4 | Distinctive testbed or later paper |
| Journal-culture KG compression | 4 | 4 | 3 | 4 | 3 | Applied case study |

Scale:

- 5 = strong;
- 3 = workable but needs design;
- 1 = weak or unclear.

Risk means execution and framing risk. Lower is better.

## First Experiment Recommendation

Start with:

```text
Provenance-preserving compressed KG packets for SLM decision support.
```

### Minimum Viable Fixture

30 to 50 graph records. Each record includes:

- claim;
- source;
- source type;
- evidence lineage;
- support status;
- uncertainty;
- related entities or concepts;
- decision question;
- expected answer boundary.

### Baseline Conditions

1. Raw text context.
2. Uncompressed graph neighborhood.
3. Generic text summary.
4. Compressed provenance-preserving graph packet.

### Primary Metrics

- answer correctness;
- unsupported-claim rate;
- provenance retention;
- decision stability under graph perturbation;
- context length;
- human audit time.

### Success Signal

The compressed graph packet should let an SLM answer with comparable or better correctness while reducing unsupported claims and preserving a reconstructable evidence path.

### Falsification Signal

The idea should be revised if compression removes evidence needed for expert judgment, causes unstable decisions, or produces better-looking but less auditable answers.

## First Paper Shape

Possible title:

```text
Provenance-Preserving Knowledge Graph Compression for Small-Model Decision Support
```

Contribution structure:

1. Define the compression objective.
2. Define a graph packet schema.
3. Build a small public or synthetic benchmark.
4. Compare SLM reasoning across raw text, uncompressed graph, generic summary, and provenance-preserving packet.
5. Report correctness, provenance retention, unsupported-claim rate, decision stability, and audit cost.

## Immediate Next Actions

1. Ask experts to choose the primary framing.
2. Select the first domain.
3. Freeze the graph packet schema.
4. Build 30 to 50 fixture records.
5. Run two SLMs and one larger model as reference.
6. Audit outputs with a claim-evidence rubric.

