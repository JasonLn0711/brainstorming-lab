# One-Page Summary

## Working Title

Evidence-preserving compressed knowledge graphs for small-model decision stability.

## Core Thesis

Small language models can become more useful for expert decision support when they receive a compressed knowledge graph that preserves evidence lineage, uncertainty, latent state, and task-relevant paths instead of receiving either a raw large graph or a generic text summary.

## Why This Is Worth Expert Review

Most `KG + SLM` work can easily collapse into a standard engineering stack: build a graph, retrieve subgraphs, prompt a small model, report QA accuracy. This packet proposes a different starting point:

```text
Knowledge graph compression is not only size reduction.
It is the design of a bounded reasoning substrate for a small model.
```

The current brainstorming repo contains several non-obvious angles that can shape a distinctive research program:

- Externalized cognition: a graph as a distributed external memory interface.
- Pheromone / Physarum flow: compression through reinforcement, diffusion, decay, and backup paths.
- Evidence provenance: compression that preserves claim lineage and forensic reliability.
- Ancient-script archaeology: low-resource symbol systems as a testbed for evidence-grounded hypothesis ranking.
- Transformer succinctness: compact representations create large implicit behavior spaces and verification demands.
- Hidden state thinking: compressed graphs should support latent-state inference, not only fact lookup.
- Journal intelligence: knowledge compression can model implicit culture, trust, and reviewer expectations.
- JANUS research compression: complex systems must be compressed into a few measurable research constructs.

## Candidate Research Directions

1. **Provenance-preserving KG compression for SLM reasoning**
   - Compress graph structure while preserving source lineage, uncertainty, support level, and claim risk.
   - Best fit for forensic, RAG trust, cybercrime evidence, and scientific evidence audit.

2. **Pheromone-based dynamic KG compression for SLM context selection**
   - Treat graph edges as living signals with reinforcement, diffusion, and decay.
   - Best fit for evolving knowledge systems, reviewer-limited discovery, and long-horizon agent memory.

3. **Latent-state KG compression for decision support**
   - Convert observable traces into compressed state trajectories that a small model can reason over.
   - Best fit for decision stability, risk escalation, high-stakes workflow support, and hidden-state modeling.

4. **Low-resource symbolic KG compression for hypothesis ranking**
   - Use ancient scripts or sparse scientific domains as a testbed where the model must rank hypotheses without overclaiming.
   - Best fit for evidence-grounded reasoning and uncertainty display.

## Recommended First Experiment

Build a small fixture with 30 to 50 claim-centered graph records:

```text
claim -> evidence source -> lineage -> uncertainty -> related concepts -> decision question
```

Compare:

1. Raw text context + SLM.
2. Retrieved uncompressed KG neighborhood + SLM.
3. Compressed provenance-preserving KG packet + SLM.

Primary measurements:

- answer correctness under evidence constraints;
- unsupported-claim rate;
- provenance retention;
- decision stability under graph compression;
- human audit time;
- context token budget.

## Main Expert Questions

- Is the core scientific object better framed as graph compression, evidence-preserving context construction, or small-model decision stability?
- Which domain gives the cleanest first test: forensic provenance, RAG trust, ancient-script hypothesis ranking, or personal/expert knowledge systems?
- What baseline would experts consider fair and convincing?
- What must be preserved during compression for the result to remain scientifically meaningful?

