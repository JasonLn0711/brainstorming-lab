# Decision Record: Expert Response On KG Compression + SLM Research Line

Date: 2026-06-01

Status: accepted as research-line narrowing guidance

## Decision

The expert recommendation is to pursue the direction after narrowing.

The research line should not be named generically as:

```text
Knowledge Graph Compression + SLM
```

The recommended framing is:

```text
Provenance-bounded evidence graph packets for stable small-model decision support.
```

## Core Research Object

The protected scientific object is:

```text
provenance-bounded compressed evidence graph packet
```

This object combines:

- packet schema;
- compression objective;
- SLM behavior under evidence-preserving compressed context.

## First Paper Direction

First paper:

```text
Provenance-Bounded Graph Packets: Evidence-Preserving Context Construction for Stable Small-Model Decision Support
```

The first paper should combine Direction A with the minimal evaluation layer of Direction C:

```text
provenance-preserving compression
-> SLM answer discipline
-> decision stability
```

Directions B and D remain roadmap items.

## Required Packet Fields

The expert marked these as the six most important fields:

```text
source_span
support_relation
evidence_force
lineage_depth
uncertainty
counterevidence_flag
```

A packet that does not preserve these fields risks becoming ordinary GraphRAG context.

## Recommended First Experiment

Domain:

```text
scientific-paper claim audit
```

Dataset path:

- Start from SciFact-style claim/evidence records.
- PubMedQA can be a second source.
- Avoid clinical-deployment framing.

Minimum pilot:

- 30 to 50 claim-centered records.
- Construct evidence graphs.
- Compare raw text, top-k text, generic summary, uncompressed graph neighborhood, random/centrality-pruned graph, and provenance-bounded compressed graph packet.
- Use two `<10B` SLMs plus one larger reference model.

## Must-Have Baselines

```text
raw text + SLM
generic summary + SLM
top-k retrieved text + SLM
uncompressed graph neighborhood + SLM
random graph pruning + SLM
centrality graph pruning + SLM
gold human/dataset label reference
```

## Primary Metrics

```text
unsupported-claim rate
provenance retention
citation lineage preservation
answer / decision correctness
uncertainty preservation
decision stability / label flip rate
```

## Scope Controls

The first paper should avoid:

- truth-verification claim;
- clinical/legal/security deployment claim;
- universal compression-improves-reasoning claim;
- GraphRAG replacement claim;
- ancient-script decipherment claim;
- claim that citation presence equals evidence support.

The positive claim should be:

```text
In bounded evidence-audit tasks, provenance-preserving compressed graph packets can reduce unsupported claims and improve evidence-lineage retention for small language models under a fixed context budget.
```

## Roadmap

```text
Paper 1: Provenance-bounded graph packets for SLM decision stability.
Paper 2: Latent-state evidence graph packets for high-risk workflow triage.
Paper 3: Adaptive / pheromone graph packet selection under repeated expert feedback.
Paper 4: Low-resource symbolic hypothesis ranking with multimodal evidence graph packets.
```

Research-line trajectory:

```text
static evidence packet
-> decision stability
-> dynamic adaptation
-> sparse symbolic generalization
```

## Three-Month Action Plan

| Window | Action |
| --- | --- |
| Week 1-2 | Freeze packet schema, annotation rubric, and 40-record SciFact pilot set. |
| Week 3-4 | Implement graph construction and six baselines. |
| Week 5-6 | Run two SLMs with fixed prompts, repeated seeds, and context-order perturbations. |
| Week 7-8 | Human audit unsupported claims, provenance retention, uncertainty preservation. |
| Week 9-10 | Run ablations removing provenance, uncertainty, counterevidence, and compression log fields. |
| Week 11-12 | Write paper draft with claim-boundary section, related-work differentiation, and failure analysis. |

## Decision State

```text
[ ] pursue now
[x] pursue after narrowing
[ ] park for later
[ ] reject / not enough research value
```

Operational interpretation:

```text
Start the pilot now, but only with A + C minimal version.
Keep B and D in the roadmap.
```

