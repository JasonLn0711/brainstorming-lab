# Clustering Logic

## Inputs

`scripts/generate_clusters.py` reads active YAML ideas under `ideas/raw`,
`ideas/evolving`, `ideas/structured`, and `ideas/executing`.

## Relationship Score

Clusters are built from pairwise merge-readiness scores. The score compares
normalized problem similarity, semantic similarity, tags, complementary value,
evidence alignment, and complexity control.

## Cluster Formation

An edge is created when the merge score is at least 60/100. Connected components
with at least two ideas become active clusters.

## Output

`clusters/active_clusters.yaml` uses generated IDs:

```yaml
cluster_0001:
  theme: ai-triage / evidence-routing
  cluster_type: research_cluster
  ideas:
    - idea_000001
    - idea_000002
  normalized_problem: "Given ..."
  average_maturity_score: 74/100
  cluster_score: 82/100
  reason:
    - normalized problem statements are similar
  recommendation: evaluate as research candidate
```
