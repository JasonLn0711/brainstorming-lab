# Clustering Logic

## Inputs

`clustering/auto_cluster.py` reads every YAML idea under `ideas/`.

## Similarity

The dependency-free engine tokenizes title, summary, problem statement, tags,
assumptions, insights, next steps, and source. Tags and title terms receive more
weight because they are intentional signals.

## Graph Edges

`graph/build_graph.py` creates an edge when at least one rule matches:

- manual connection in `connections`
- shared tags
- token-vector semantic similarity above `similarity_threshold`

## Cluster Formation

Clusters are connected components over manual-connection and semantic-similarity
edges. Shared-tag edges remain visible in the graph but do not automatically
force clusters, which keeps broad tags from merging unrelated ideas too early.

## Output

`clustering/clusters.yaml` uses stable generated IDs:

```yaml
cluster_001:
  theme: ai-triage / evidence-routing
  ideas:
    - idea_000001
    - idea_000002
  avg_score: 14.0
  size: 2
```
