# Expert Brief

## Purpose

This packet records a research direction around `Knowledge Graph Compression + SLM` and translates existing brainstorming notes into expert-reviewable hypotheses, candidate experiments, and decision questions.

The goal is to help experts judge:

- whether the direction has a defensible scientific object;
- which framing is strongest;
- which first experiment is feasible;
- which claims should be avoided until evidence exists.

## Positive Research Framing

The strongest current framing is:

```text
Evidence-preserving compressed knowledge graphs can provide small language models with a bounded, auditable reasoning substrate for decision support.
```

This framing treats graph compression as a research object with four operating requirements:

1. **Relevance compression**: the model receives the part of the graph needed for the current question.
2. **Evidence preservation**: the compression keeps source lineage, support level, and uncertainty.
3. **Decision stability**: the model's answer remains stable when irrelevant graph detail is removed.
4. **Auditability**: a reviewer can reconstruct why the model used a claim, path, or source.

## Why This Is Not Just GraphRAG

The proposed direction differs from a generic GraphRAG pipeline in its research target.

Generic GraphRAG often asks:

```text
Can graph retrieval improve answer quality?
```

This packet asks:

```text
What must a compressed graph preserve so a small model can reason with evidence, uncertainty, and decision stability?
```

The research contribution can therefore live in:

- compression objective design;
- provenance-aware graph packet construction;
- uncertainty and hidden-state representation;
- evaluation of decision stability under compression;
- expert-auditable evidence trails.

## Source Thinking From The Brainstorming Repo

### Externalized Cognition OS

The repo's cognition-OS idea argues that the strongest architecture is not one giant memory store, but distributed canonical homes connected by thin planning bridges. This maps naturally to KG compression:

```text
large external memory -> canonical source nodes -> thin task packet -> SLM reasoning
```

Research implication:

The graph should not be a warehouse. It should be a structured external memory layer that can generate compact, task-specific reasoning packets.

### Pheromone / Physarum Flow

The ant-colony and Physarum notes frame graph behavior as local reinforcement, diffusion, decay, and adaptive flow. This suggests a nonstandard compression method:

```text
edge value = recent utility + evidence strength + task relevance + reinforcement - decay
```

Research implication:

Graph compression can be dynamic. Instead of permanently pruning the graph, the system can expose a temporarily reinforced subgraph to the SLM while preserving backup paths for robustness.

### Evidence Provenance

The evidence-provenance thread defines the scarce resource as verifiable evidence provenance, not more fluent summaries. This is central to expert-facing KG compression.

Research implication:

A compressed graph must preserve the difference between:

- primary evidence;
- authoritative synthesis;
- human synthesis;
- AI-like synthesis;
- circular citation;
- unverifiable claim;
- unrelated citation.

Compression that removes provenance may improve token efficiency while damaging scientific reliability.

### Ancient Script And Archaeology

The ancient-language idea reframes AI support as evidence-grounded restoration and hypothesis ranking under sparse data, missing anchors, and high uncertainty.

Research implication:

Low-resource symbolic domains are strong testbeds because the model cannot rely on fluent pretrained knowledge alone. The system must preserve sign sequence, artifact context, date range, provenance, and uncertainty.

### Transformer Succinctness

The transformer-succinctness note highlights a formal lesson: compact representations can encode very large implicit behavior spaces. This gives a useful caution for KG + SLM research.

Research implication:

Compression increases power and risk at the same time. A compressed graph packet must be evaluated not only for answer quality, but also for what behavior space it permits the SLM to infer.

### Hidden State Thinking

The hidden-state methodology says that important states are often unavailable as direct observations; analysts see traces and infer state trajectories.

Research implication:

The target of compression may be a latent state graph, not a fact graph:

```text
observable traces -> compressed state representation -> SLM decision support
```

This is especially relevant for risk escalation, scam cognition, institutional stress, and high-stakes triage.

### Journal Intelligence

The journal-intelligence idea studies accepted papers as evidence of latent reviewer standards and scientific trust formation.

Research implication:

KG compression can model implicit culture. A compressed graph may represent evidence standards, trust signals, reviewer fear points, and claim-boundary norms rather than only entities and relations.

### JANUS Research Compression

The JANUS note provides a meta-rule: a growing engineering universe must be compressed into a few research constructs. For KG + SLM, this means avoiding a stack-shaped project and choosing one measurable thesis.

Recommended thesis:

```text
Small models make more stable expert-support decisions when their context is a provenance-preserving compressed graph rather than raw text or an uncompressed graph neighborhood.
```

## Candidate Contribution Statement

This work defines and evaluates a provenance-preserving knowledge graph compression method for small-model decision support. The method converts large, heterogeneous evidence graphs into compact reasoning packets that preserve source lineage, uncertainty, latent-state cues, and task-relevant paths. The evaluation tests whether small language models using these packets produce more auditable and stable decisions than models using raw text context or uncompressed graph neighborhoods.

## Scope Controls

The first study should stay within a bounded expert-review context:

- public or synthetic evidence only;
- no clinical, legal, or operational deployment claim;
- no claim that SLMs independently verify truth;
- no claim that graph compression is universally optimal;
- no claim that ancient-script or forensic domains are solved.

The positive operating scope is:

```text
expert-support reasoning over bounded evidence graphs with traceable compression.
```

