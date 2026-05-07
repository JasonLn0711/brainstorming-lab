# Maturity Model

The Idea OS uses one strict 100-point maturity score. The old compact score is
not a decision input.

## Dimensions

| Dimension | Points | What It Measures |
| --- | ---: | --- |
| Problem clarity | 15 | Raw problem, normalized problem, and Given/optimize/constraints structure |
| Boundary definition | 10 | Tags, scope constraints, and explicit limitations |
| Testability | 15 | Baseline, metrics, input/output shape, and experiment next step |
| Evidence support | 15 | Observations, concrete cases, data, literature, and real-world need |
| Connection strength | 10 | Manual links, shared tags, and cluster membership |
| Novelty | 10 | Whether the idea is duplicate, variation, new method, or original angle |
| Feasibility | 15 | Prototype path, available tools, one-week testability, and operational risk |
| Research potential | 10 | Research question, evaluation metric, contribution, and paper/prototype path |

Each idea stores numeric values and display strings:

```yaml
maturity:
  problem_clarity: 12
  problem_clarity_score: 12/15
maturity_score: 74/100
maturity_level: research_candidate
```

## Levels

| Score | Level | Action |
| --- | --- | --- |
| 0-20/100 | `raw` | Keep as raw idea |
| 21-40/100 | `emerging` | Clarify and normalize problem statement |
| 41-60/100 | `structured` | Include in graph and clustering |
| 61-80/100 | `research_candidate` | Evaluate cluster readiness |
| 81-100/100 | `execution_ready` | Generate experiment plan |

## Examples

An idea with only a title and a vague summary will usually stay `raw` or
`emerging`. An idea with a normalized problem, baseline, metrics, evidence, and
connected neighbors can become `research_candidate`. An `execution_ready` idea
needs enough testability and feasibility to support an experiment plan.
