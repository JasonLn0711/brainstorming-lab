# Research Directions

## Direction A: Provenance-Preserving KG Compression For SLM Reasoning

### Core Question

What graph information must be preserved during compression so a small language model can answer with evidence discipline and avoid unsupported claims?

### Proposed Object

```text
compressed evidence packet = claim nodes + support paths + source lineage + uncertainty + task-relevant concepts
```

### First Experiment

Create 30 to 50 claim-centered graph records from a bounded public domain.

Compare:

- raw source snippets;
- uncompressed graph neighborhood;
- compressed provenance-preserving graph packet.

Ask an SLM to answer evidence-sensitive questions.

### Metrics

- unsupported-claim rate;
- provenance retention;
- answer correctness;
- citation-lineage preservation;
- human audit time;
- token budget;
- confidence calibration.

### Strong Domains

- RAG trust and web evidence pollution;
- cybercrime or scam-prevention public evidence;
- scientific-paper claim audit;
- journal intelligence packets.

### Expert Review Need

Experts should decide which provenance fields are essential and which domain provides clean, ethical, public evidence.

## Direction B: Pheromone-Based Dynamic KG Compression

### Core Question

Can dynamic reinforcement, diffusion, and decay select better graph substructures for small-model reasoning than static top-k retrieval?

### Proposed Object

```text
edge_score(t+1) = reinforcement + diffusion - decay + evidence_weight + task_relevance
```

### First Experiment

Build a synthetic or repo-derived knowledge graph where queries recur over time. Track which paths are used, corrected, reinforced, or decayed.

Compare:

- static top-k graph retrieval;
- PageRank-like centrality;
- pheromone-style dynamic compression;
- full graph neighborhood.

### Metrics

- answer quality over repeated tasks;
- stability after topic drift;
- recovery after stale-path decay;
- backup-path preservation;
- reviewer correction uptake;
- context budget.

### Strong Domains

- long-horizon agent memory;
- expert note systems;
- literature review routing;
- scam-candidate discovery;
- evolving project knowledge.

### Expert Review Need

Experts should assess whether this is a meaningful compression contribution or better framed as adaptive retrieval.

## Direction C: Latent-State KG Compression For Decision Support

### Core Question

Can observable graph traces be compressed into latent-state representations that support more stable small-model decisions?

### Proposed Object

```text
trace graph -> latent state graph -> decision packet -> SLM recommendation
```

### First Experiment

Use a small public or synthetic high-stakes workflow dataset. Encode events, signals, and evidence as a graph. Compress the graph into state hypotheses and ask the SLM to make bounded recommendations.

### Metrics

- decision stability under graph compression;
- label flip rate;
- unsafe downrouting or missed escalation in synthetic cases;
- evidence-to-state traceability;
- uncertainty reporting quality;
- expert audit burden.

### Strong Domains

- ASR decision-stability;
- scam cognitive-state modeling;
- institutional stress modeling;
- medical-intake synthetic demo;
- workflow triage.

### Expert Review Need

Experts should decide whether the first paper should focus on hidden-state inference, graph compression, or SLM decision stability.

## Direction D: Low-Resource Symbolic KG Compression

### Core Question

Can compressed multimodal evidence graphs help a small model rank hypotheses in sparse symbolic domains without overclaiming?

### Proposed Object

```text
symbol record + artifact context + co-occurrence graph + uncertainty + bibliography -> hypothesis packet
```

### First Experiment

Build a toy benchmark that contrasts:

- known-language restoration;
- undeciphered-script structure analysis.

The SLM must output ranked hypotheses, uncertainty notes, and evidence paths rather than translations.

### Metrics

- hypothesis-grounding quality;
- overclaim avoidance;
- uncertainty clarity;
- preservation of artifact context;
- expert review usefulness.

### Strong Domains

- ancient inscriptions;
- scientific notation systems;
- low-resource technical taxonomies;
- sparse cyber evidence traces.

### Expert Review Need

Experts should decide whether the domain is too far from the main research identity or valuable as a distinctive testbed.

## Recommended First Choice

The strongest first direction is Direction A with elements of Direction C:

```text
Provenance-preserving compressed knowledge graphs for small-model decision stability.
```

This is the best balance of:

- connection to existing repo strengths;
- expert-review value;
- measurable experiment design;
- clear boundary from generic GraphRAG;
- publishable research object.

