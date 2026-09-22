# Experiment Design Record: Data, Benchmarks, Metrics, And Pilot Plan

Date: 2026-06-01

Status: accepted as first-pilot design guidance

## Decision

The first paper should use public datasets as the main experiment and keep private or self-owned data as case study material.

Primary reason:

```text
Public datasets support reproducibility, comparison, reviewer challenge, and benchmark grounding.
Private data supports external validity and real-workflow demonstration, but should not carry the first method claim.
```

## Research Question

The first paper should not be designed as a generic summarization benchmark.

The sharper research question is:

```text
Under a fixed token budget, can provenance-preserving compressed evidence graph packets help sub-10B small language models produce fewer unsupported claims, retain more evidence lineage, and maintain more stable decision labels than raw text, summaries, retrieval snippets, or generic graph pruning?
```

## Three-Layer Data Strategy

| Layer | Data Type | Role |
| --- | --- | --- |
| Layer 1 | Public claim/evidence datasets | Main experiment, quantitative evidence, reproducibility |
| Layer 2 | Controlled synthetic or semi-synthetic stress set | Compression mechanism, counterevidence retention, distractors, label flip tests |
| Layer 3 | Private or self-owned data | External validity, real-scenario case study, later paper |

First-paper claims should rely on Layer 1 and Layer 2. Layer 3 can appear as an appendix or external-validity pilot only.

## Recommended Dataset Roadmap

### First Paper Main Data

```text
SciFact + FEVEROUS
```

SciFact is the first choice because it is a scientific claim verification dataset with claims, evidence-containing abstracts, support/refute labels, and rationales.

FEVEROUS is the second choice because it includes text and table evidence and can test structured provenance.

### Secondary Data

```text
Qasper or PubMedQA
```

Qasper is useful for full-paper evidence QA and long-document evidence preservation. PubMedQA is useful for yes/no/maybe decision labels but has weaker provenance structure.

### Meeting Extension

```text
QMSum / MeetingBank
```

These are useful for a meeting-decision extension but require manual annotation for decision spans, action items, speaker roles, evidence spans, uncertainty, and decision boundaries.

### Private Data

Private meeting, medical-intake, or scam workflow data should be used only as external validation or a later paper unless a de-identification, ethics, access, and annotation protocol is ready.

## Derived Benchmark

The project should build a derived benchmark rather than inventing a private-only benchmark or forcing summarization metrics into the main role.

Working name:

```text
PB-EGP-50
Provenance-Bounded Evidence Graph Packet Benchmark
```

Each record should contain:

```text
claim / question
source document
gold evidence span
gold decision label
candidate evidence graph
compressed packet
model output
audit annotation
```

## Primary Metrics

The first paper's primary metrics should be:

```text
decision correctness
unsupported-claim rate
provenance retention
citation lineage preservation
uncertainty preservation
decision stability / label flip rate
counterevidence retention
human audit time
```

ROUGE, BERTScore, and generic summarization metrics can be reported only as secondary or background metrics.

## Secondary And Reference Metrics

Useful supporting metrics and frameworks:

- ROUGE and BERTScore for secondary summary similarity.
- SummEval as summarization-evaluation background.
- QAFactEval, SummaC, AlignScore, and FActScore-style atomic fact checking for factual consistency.
- AIS, ALCE, and Ref-Long style citation/reference checks for attribution and referencing.
- RAGAS, ARES, and RAGTruth for RAG faithfulness comparison.
- LongBench, LongBench v2, and SummHay as long-context background or later evaluation, not first-paper main benchmark.

## Minimal Pilot

### Size

```text
40 to 50 public records
```

Recommended composition:

```text
30 SciFact support/refute records
10 to 20 FEVEROUS insufficient / mixed / table-evidence records
```

### Models

```text
1 to 2 sub-10B SLMs
1 larger reference model
```

The larger model is a reference ceiling, not gold truth.

### Context Conditions

Must-have:

```text
raw text
equal-budget raw text
top-k retrieved text
generic summary
uncompressed graph neighborhood
random graph pruning
centrality-pruned graph
provenance-bounded packet
```

Strong baseline:

```text
GraphRAG-style subgraph retrieval
```

Upper bound:

```text
oracle evidence packet
```

### Token Budgets

Use fixed budgets:

```text
512
1024
2048
```

The pilot can start with 1024 or 2048 tokens.

### Perturbations

Use:

```text
evidence order shuffle
irrelevant distractor nodes
low-authority related source
reduced budget
counterevidence stress
prompt paraphrase
```

## Graph Schema

Minimum node types:

```text
Claim
EvidenceSpan
SourceDocument
Entity / Concept
Method
Result
Limitation
Uncertainty
CounterEvidence
```

Minimum edge types:

```text
mentions
reports
measures
compares
derived_from
cites
qualifies
contradicts
supports_candidate
refutes_candidate
source_lineage
```

Required fields:

```text
claim_id
source_id
span_id
span_text
source_type
source_date
lineage_path
candidate_relation
uncertainty_tag
counterevidence_flag
compression_reason
```

## Compression Method

Use an interpretable constrained budgeted compressor first.

Input:

```text
candidate evidence graph G
task question q
token budget B
```

Output:

```text
compressed evidence graph packet P_B
```

Hard constraints:

- retain at least one source lineage path for each retained claim;
- retain direct evidence spans before background nodes;
- retain counterevidence if present;
- retain uncertainty and limitation nodes;
- retain source type and span id;
- do not merge claims with different evidence force.

Soft objectives:

- maximize task relevance;
- maximize evidence coverage;
- maximize source diversity;
- minimize redundant background;
- minimize token length.

## Evaluation Tracks

### Track A: Oracle Graph Compression

Use gold evidence spans to build the graph.

Purpose:

```text
Measure compression and packet-schema upper bound.
```

Boundary:

```text
Do not claim end-to-end deployability from oracle-only results.
```

### Track B: Predicted Graph Compression

Use retrieval and extraction to build candidate graphs:

```text
BM25 / dense retrieval
NLI model or small LLM candidate relation labeling
entity / concept extraction
packet compression
```

Purpose:

```text
Measure practical usability.
```

## Ablation Plan

Run:

```text
Full packet
- provenance
- uncertainty
- counterevidence
- compression log
- graph relation labels
- source type
- equal-token summary
```

The ablation is the defense against the critique that this is only a JSON prompt trick.

## Human Audit

Use blinded human audit for at least the pilot outputs.

Each output should be scored for:

```text
decision label correctness
atomic claim support
citation support
uncertainty retention
overclaim
missed counterevidence
audit time
```

Report:

```text
inter-annotator agreement
Cohen's kappa or Krippendorff's alpha
adjudication procedure
```

## Statistical Analysis

Use paired design because each record runs across multiple methods.

Recommended tests:

- McNemar test or paired bootstrap for decision correctness.
- Wilcoxon signed-rank test or paired bootstrap for unsupported-claim rate.
- Paired bootstrap confidence intervals for provenance retention.
- Paired comparison for label flip rate.
- Wilcoxon signed-rank test for audit time.
- Report effect sizes and confidence intervals, not only p-values.

## Four-Week Pilot Plan

| Week | Work |
| --- | --- |
| Week 1 | Select 40 to 50 records; define graph schema v0; write annotation guideline; define labels and unsupported-claim rubric. |
| Week 2 | Segment evidence spans; assign source/span IDs; build claim-evidence graphs; implement greedy packet compressor; generate 512/1024/2048-token packets and baselines. |
| Week 3 | Run 1 to 2 sub-10B SLMs and one larger reference model at temperature 0; execute context conditions; save JSON outputs. |
| Week 4 | Human audit outputs; split atomic claims; label unsupported claims; calculate provenance retention, citation precision/recall, label flip rate; write failure analysis. |

## Go / Revise / Stop Gate

Go:

```text
packet clearly lowers unsupported claims and improves provenance retention.
```

Revise:

```text
packet helps, but model instability remains high or uncertainty disappears.
```

Stop / reframe:

```text
top-k text + prompt is equally strong, or generic summary is equally strong.
```

## Formal Paper Minimum Success Condition

The first paper must show:

```text
Under the same token budget, provenance-bounded compressed graph packets produce lower unsupported-claim rates and higher provenance retention than generic summary, top-k text, and centrality-pruned graph, without reducing decision correctness.
```

Stronger claim:

```text
The packet has lower label flip rate under perturbation.
```

Strongest claim:

```text
The packet reduces human audit time while preserving counterevidence and uncertainty.
```

## Core Takeaway

```text
The first paper does not prove that small models summarize better.
It proves that small models reason with fewer boundary violations, stronger traceability, and more stable labels when given provenance-preserving compressed evidence graph packets.
```

