# Narrowed Pilot Plan: Provenance-Bounded Evidence Graph Packets

Date: 2026-06-01

Status: accepted as narrowed first-pilot plan

## Decision

The research direction remains worth pursuing, but the first paper must narrow again.

The first paper should prove only this:

```text
Under the same token budget, provenance-bounded evidence graph packets create measurable evidence-discipline gains for sub-10B models.
```

The main comparison is:

```text
provenance-bounded evidence graph packet
vs top-k text
vs generic summary
vs generic graph pruning
vs context compression
```

The paper should not attempt to solve meeting decision support, medical/scam workflows, dynamic graph memory, latent-state reasoning, or low-resource symbolic generalization in the first study.

## Recommended Framing

```text
Provenance-bounded evidence graph packet construction for stable small-model decision support.
```

Method object:

```text
provenance-bounded evidence graph packet construction
```

Target model:

```text
sub-10B small language models
```

Evaluation target:

```text
decision stability + evidence discipline
```

## Formal Object Definition

Given:

- evidence graph `G`;
- task `q`;
- token budget `B`;
- target small model family `M`;
- allowed answer space `Y`;

construct:

- packet `P_B`;

such that:

- `P_B` fits `B`;
- `P_B` preserves task-relevant evidence paths;
- `P_B` retains provenance and uncertainty;
- `P_B` exposes counterevidence and risk boundaries;
- outputs generated from `P_B` are auditable against source spans.

## Required Packet Field Groups

### Source Anchoring

```text
source_id
source_type
source_span_id
source_span_text
source_offset / sentence_id / table_cell_id
source_date_or_version
source_authority_or_origin
```

### Evidence Relation

```text
claim_id
target_claim_text
support_relation
relation_polarity
evidence_force
scope_of_support
counterevidence_flag
conflict_group_id
```

Boundary:

```text
support_relation, evidence_force, and counterevidence_flag must not leak gold labels into the main predicted-track experiment.
```

### Boundary Control

```text
uncertainty_type
uncertainty_level
limitation_note
risk_boundary
abstention_condition
unsafe_inference_warning
```

### Audit Trail

```text
lineage_path
lineage_depth
compression_operation
retained_reason
dropped_reason
dropped_counterevidence_warning
audit_reconstruction_pointer
```

## Dataset Plan

### Pilot

```text
SciFact + FEVEROUS
```

Purpose:

- fast feasibility test;
- text evidence;
- structured/table evidence;
- support/refute/insufficient;
- provenance reconstruction.

### Formal Paper

Recommended:

```text
Main: 300 SciFact records
Structured scientific supplement: 100 SciTab or FEVEROUS records
Long-document secondary: 50 Qasper records
```

PubMedQA can support yes/no/maybe decision-label stability, but should not carry the provenance claim.

QMSum and MeetingBank stay as later meeting-decision extensions.

Private data stays as external validation or later paper material.

## PB-EGP-50 Additions

The benchmark record should add:

```text
gold_lineage_path
gold_counterevidence_or_conflict
gold_boundary_note
```

These fields are required because provenance, counterevidence, and risk boundary need gold targets before output audit.

## Minimum Viable Pilot

```text
50 public records
1 primary sub-10B SLM
1 larger reference model
1 token budget first: 1024 or 2048
5-6 context conditions
2 perturbations
human audit all key outputs
```

This replaces the larger earlier pilot design with multiple budgets, many baselines, two SLMs, and many perturbations.

## Formal Paper Size

```text
300-500 records total
at least 600 outputs or 20-30% stratified outputs for human audit
```

## Must-Have Baselines

```text
equal-budget raw text + SLM
top-k retrieved text + SLM
generic summary + SLM
flat evidence list + SLM
context compression baseline + SLM
uncompressed graph neighborhood + SLM
centrality-based graph pruning + SLM
provenance-bounded graph packet + SLM
```

GraphRAG-style subgraph retrieval is optional for the pilot but required for a formal paper that explicitly differentiates from GraphRAG.

Oracle evidence packet is allowed only as an upper bound and must be clearly separated from main results.

## Evaluation Tracks

### Track A: Oracle Packet

Use gold evidence spans.

Purpose:

```text
schema / compression upper bound
```

Boundary:

```text
Do not support the end-to-end main claim with oracle-only results.
```

### Track B: Predicted Packet

Use retriever plus relation extractor / NLI / small model to build candidate graph.

Purpose:

```text
main practical claim
```

### Track C: Relation-Hidden Packet

Keep:

```text
source_span
lineage
uncertainty
source_type
```

Remove:

```text
support/refute relation labels
```

Purpose:

```text
test whether the SLM can still decide without gold-label leakage.
```

## Primary Metrics

Formal paper primary metrics should be reduced to four:

```text
unsupported-claim rate
provenance / citation validity
decision correctness
decision stability under non-evidential perturbation
```

## Secondary Metrics

```text
uncertainty preservation
counterevidence retention
human audit time
compression ratio
context token budget
QAFactEval / SummaC / AlignScore
FActScore-style factuality
RAGAS / ARES faithfulness
ROUGE / BERTScore
```

## Unsupported-Claim Audit Labels

Use atomic-claim audit labels:

```text
SUPPORTED_BY_CITED_SPAN
SUPPORTED_BY_PACKET_BUT_BAD_CITATION
CONTRADICTED_BY_EVIDENCE
NOT_IN_PACKET
OVERGENERALIZED
UNCERTAIN_BUT_STATED_AS_CERTAIN
UNVERIFIABLE_OR_EXTERNAL_KNOWLEDGE
```

Unsupported-claim rate:

```text
(CONTRADICTED + NOT_IN_PACKET + OVERGENERALIZED + UNCERTAIN_AS_CERTAIN + UNVERIFIABLE)
/
total atomic claims
```

## Provenance Retention

Use set overlap, not subjective impression.

Gold lineage set:

```text
source_id
span_id
sentence_id / table_cell_id
section_id
source_type
lineage_path
```

Output-level citation validity:

```text
citation precision = valid cited spans / all cited spans
citation recall = atomic claims with valid citation / atomic claims requiring citation
```

## Decision Stability

Separate perturbation types.

### Non-Evidential Perturbations

Label should not change:

```text
evidence order shuffle
JSON field order shuffle
irrelevant distractor node
prompt paraphrase
equivalent serialization
```

Metric:

```text
Invariance stability = 1 - label flip rate under non-evidential perturbations
```

### Evidential Perturbations

Label may change or uncertainty should increase:

```text
remove direct evidence
add counterevidence
reduce budget until key evidence missing
add low-authority conflicting source
```

Metric:

```text
Evidence sensitivity = correct adjustment rate under evidential perturbations
```

## Key Perturbations

```text
evidence order shuffle
serialization change
irrelevant distractor nodes
prompt paraphrase
low-authority related source
counterevidence insertion
budget reduction
field-name perturbation
```

Serialization formats:

```text
JSON
YAML-like bullet list
plain evidence table
```

## Key Ablations

```text
remove provenance
remove uncertainty
remove counterevidence
remove relation labels
remove source type
remove compression log
flat evidence list
same-token generic summary
same packet rendered as non-JSON
relation-hidden packet
gold evidence spans only
predicted evidence spans only
```

Most important comparison:

```text
full packet
vs flat evidence list
vs same-token generic summary
vs same-token top-k text
```

## Human Audit

Pilot:

```text
2 annotators
audit all key outputs for 1 primary SLM
5-6 context conditions only
```

Formal paper:

```text
2 annotators minimum
3 preferred with adjudication
20-30% stratified outputs or at least 600 outputs
```

Report:

```text
Cohen's kappa
Krippendorff's alpha where appropriate
percent agreement
adjudicated final labels
```

## Statistical Analysis

Use paired design plus optional mixed-effects analysis.

Recommended:

```text
McNemar / paired bootstrap for decision correctness
Wilcoxon / paired bootstrap for unsupported-claim rate
paired bootstrap CI for provenance retention
paired comparison for label flip rate
Wilcoxon for audit time
mixed-effects model as auxiliary analysis
Holm-Bonferroni or Benjamini-Hochberg correction
effect sizes and confidence intervals
```

## Hard Go / No-Go Gate

### Go

Proceed if:

```text
packet beats top-k retrieved text on unsupported-claim rate
packet beats generic summary on provenance retention
packet beats flat evidence list or context compression on at least one primary metric
decision correctness does not drop meaningfully
full packet beats key ablations
gains appear in predicted-track setting, not only oracle setting
```

Target thresholds:

```text
unsupported-claim rate relative reduction >= 20%
provenance retention absolute gain >= 10 points
decision correctness drop <= 3 points
label flip rate reduction >= 10-15%
counterevidence retention >= 75% on stress subset
```

### Revise

Revise if:

```text
packet lowers unsupported claims but loses uncertainty
packet improves provenance but hurts correctness
benefit only appears with relation labels
benefit disappears under serialization perturbation
human audit agreement is low
small model ignores citation / uncertainty fields
```

### Stop / Reframe

Stop or reframe if:

```text
top-k text + strong prompt equals packet
flat evidence list equals packet
context compression baseline equals packet
oracle packet works but predicted packet fails badly
full packet does not beat remove-provenance / remove-uncertainty ablations
gains come only from leaking support/refute labels
counterevidence is systematically dropped
human audit cannot reliably apply the rubric
```

## Three-Month Execution Plan

| Window | Action |
| --- | --- |
| Weeks 1-2 | Freeze schema v0; define gold lineage; write audit rubric; select 50 pilot records from SciFact + FEVEROUS; prepare source/span IDs. |
| Weeks 3-4 | Build oracle graph and predicted candidate graph; implement greedy packet compressor; implement equal-budget text, top-k text, generic summary, flat evidence list, centrality pruning, and context compression baselines. |
| Weeks 5-6 | Run one sub-10B SLM and one larger reference model at temperature 0; use one token budget first; run evidence-order shuffle and distractor-node perturbations. |
| Weeks 7-8 | Human audit primary outputs; compute unsupported-claim rate, provenance retention, citation validity, decision correctness, and label flip rate; adjudicate disagreements. |
| Weeks 9-10 | Run ablations removing provenance, uncertainty, counterevidence, relation labels, source type, and compression log; run serialization perturbation. |
| Weeks 11-12 | Analyze paired results; write failure analysis; decide whether to scale to 300-500 records; prepare workshop / arXiv draft if pilot clears gate. |

