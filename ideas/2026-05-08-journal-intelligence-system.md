# Journal Intelligence System

Date: 2026-05-08

Canonical YAML:

```text
ideas/structured/idea_000014_journal_intelligence_system.yaml
```

## First-Principle Read

The scarce resource is not access to more papers. The scarce resource is
submission cycles, reviewer trust, and revision energy.

Author guidelines explain the formal boundary. Recent accepted papers reveal
part of the venue culture:

- what claims are allowed to sound strong
- what evidence is considered enough
- what figures reviewers expect to inspect
- what novelty type the journal rewards
- what failure modes the editor/reviewer ecosystem fears
- what citation tribe and terminology the venue lives inside

The useful object is not a PDF pile. The useful object is a venue-fit
calibration packet that can change a manuscript before submission.

## Core Idea

Use recent accepted Open Access papers from a target journal to reverse-engineer
latent venue standards.

This does not replace:

- author guidelines
- ethical publishing rules
- scientific quality
- advisor judgment
- real reviewer feedback

It adds an evidence-driven layer:

```text
author guide + recent accepted OA papers + citation ecosystem
-> journal culture brief
-> latent scoring matrix
-> manuscript compatibility report
-> revision priorities
```

## What To Extract

### Claim Style

Measure whether accepted papers tend to say:

- `We propose`
- `We investigate`
- `We analyze`
- `We demonstrate`
- `may`
- `could`
- `practical`
- `operational`
- `real-world`

For forensic, medical, and security venues, aggressive language can create risk.
Conservative language may be a trust signal.

### Figure Style

Track:

- figure count
- architecture diagrams
- workflow diagrams
- evidence trace tables
- qualitative case studies
- ablation charts
- graphical abstracts
- large overview figures

Figure style is often a hidden venue-fit signal. It reveals what evidence the
reviewer expects to see at a glance.

### Evidence Density

Track:

- baseline count
- ablation count
- failure analysis
- limitation section
- threat model
- supplementary material
- reproducibility assets
- appendix length

This approximates the venue's minimum credibility threshold.

### Novelty Type

Classify accepted papers by the type of novelty they reward:

- engineering novelty
- forensic novelty
- governance novelty
- evaluation novelty
- theoretical novelty
- application-impact novelty

This matters because "novelty" is not one thing. FSI:DI-style venues may value
forensic defensibility and evidence workflow more than model architecture.

### Reviewer Fear Points

The higher-level question is not only what the journal likes. It is what the
journal fears.

Possible fear points:

- overclaim
- unverifiable evidence
- unrealistic simulation
- AI hallucination
- non-reproducible workflow
- weak forensic defensibility
- missing operational boundary
- unsupported generalization

Repeated limitation wording, conservative claims, traceability language, and
reproducibility emphasis can expose the reviewer ecosystem's defense mechanism.

### Citation Ecosystem

Track recurring:

- authors
- venues
- methods
- terminology
- datasets
- skepticism patterns
- evaluation philosophy

A journal is not only a publisher. It is an editor, reviewer tribe, accepted
narrative style, and citation ecosystem.

## First Calibration Packet

For one target journal, collect 8-12 recent accepted Open Access papers plus the
official author guide.

Create a CSV with:

```text
paper_id
year
article_type
claim_style
figure_style
evidence_density
novelty_type
reviewer_fear_points
reproducibility_assets
limitation_style
compatibility_lessons
```

Then write a short journal culture brief:

- formal scope
- accepted contribution patterns
- common evidence shape
- claim-language boundary
- figure/table expectation
- top reviewer fear points
- likely rejection risks
- revision checklist for our manuscript

## Reviewer Emulator

Input:

```text
paper.md
target journal
journal culture packet
```

Output:

```text
Venue compatibility: 0-100
Main risks:
- overclaim risk
- evidence-density gap
- figure/table gap
- reproducibility gap
- novelty-type mismatch
- missing limitation or threat-model discussion
Revision priorities:
- strengthen
- soften
- add
- remove
- reframe
```

## FSI:DI Fit

This is especially useful for FSI:DI because the venue likely cares about:

- forensic defensibility
- traceability
- reproducibility
- conservative claims
- failure analysis
- operational realism
- governance boundary
- evidence integrity

The first concrete test should reuse the existing FSI:DI latest-OA calibration
work and turn it into a reusable journal-culture brief.

## Safety Boundary

Use only public OA papers, official guidelines, and legitimate metadata.

Do not:

- bypass paywalls
- scrape private reviewer/editor systems
- claim hidden reviewer identity
- claim guaranteed acceptance
- pretend OA samples fully represent the whole journal

Separate:

- observed evidence
- inferred pattern
- uncertainty
- revision implication

## Smallest Next Test

Build one FSI:DI venue-culture calibration packet from 8-12 recent accepted OA
papers plus the official author guide.

Done condition:

- one CSV pattern matrix
- one 1-2 page journal culture brief
- one compatibility checklist for the current FSI:DI manuscript line
- one decision: proceed, revise-first, park, or choose another venue

## Method Decision: Do Not Start With Deep Learning

Machine learning and deep learning are possible later, but they are not the
first move.

The first 80% of value is not the classifier. It is:

- feature engineering
- rubric design
- scientometric thinking
- reviewer psychology modeling
- latent structure extraction
- deciding what is worth observing

The common failure mode is too-early AI:

```text
3000 papers -> embeddings -> clustering -> LLM summary
```

The output often becomes:

```text
This journal values rigorous experiments.
```

That is too abstract. It does not tell us what to strengthen, soften, add,
remove, or reframe in the manuscript.

Reviewer-sensitive signals often live in small details:

- claim wording
- limitation placement
- figure order
- appendix density
- operational boundary wording
- `we deploy` vs `we simulate`
- evidence-chain description
- failure-analysis placement

If those features are not defined first, AI will often miss the useful signal.

## Journal Forensic Framework

The first phase should be a quantifiable observation system:

```text
schema + rubric + feature extraction + human interpretation
```

Seed schema:

| Category | Feature |
| --- | --- |
| claim | aggressive / conservative / investigative |
| evidence | weak / moderate / strong / traceable |
| reproducibility | code, protocol, parameters, dataset availability |
| dataset realism | synthetic / public / private / operational |
| figures | workflow, table, chart, case study, architecture, evidence trace |
| evaluation | ablation, baseline, statistical test, failure analysis |
| language | may, could, practical, deploy, prove, demonstrate |
| trust signals | limitation, threat model, governance boundary, operational realism |

This is closer to forensic investigation than generic paper summarization.

The hard question is:

```text
What should be observed?
```

not:

```text
Which model should classify the papers?
```

## Accepted Manifold, Not Acceptance Prediction

This idea is better framed as latent reviewer space extraction.

We usually have:

```text
accepted papers
```

but not:

```text
rejected papers + reviewer comments
```

So supervised acceptance prediction is structurally weak. The data has serious
selection bias.

Instead, estimate an accepted-paper distribution:

- what accepted papers sound like
- what evidence they contain
- what they avoid claiming
- what figures they use
- what risks they preempt
- what limitations they acknowledge

Then compare our draft against that distribution.

The goal is not:

```text
acceptance probability = 0.71
```

The goal is:

```text
High reviewer risk:
- insufficient threat model
- weak operational boundary
- overclaim wording
- no failure vignette
- synthetic realism not defended enough
```

That output is more honest and more useful.

## Hybrid Intelligence

The practical architecture should be:

```text
rule-based extraction + LLM assistance + human scientific interpretation
```

Layer 1: metadata extraction.

- title
- abstract
- keywords
- section structure
- figure count
- table count
- appendix
- supplementary material

Layer 2: scientific feature extraction.

- claim aggressiveness
- evidence density
- reproducibility
- operational realism
- limitation style
- reviewer fear points

Layer 3: human interpretation.

Reviewer culture is context-dependent. FSI:DI may react very differently to a
synthetic dataset than NeurIPS, IEEE TIFS, or a general AI journal.

AI can assist the extraction, but the interpretation has to remain scientific
and domain-aware.

## When ML Becomes Useful

ML becomes useful after the schema stabilizes and there are enough calibrated
examples.

Useful later layers:

- embedding-based nearest accepted-paper search
- clustering accepted papers into contribution families
- topic drift detection
- novelty fatigue detection
- draft-to-venue similarity ranking
- reviewer-risk retrieval from prior calibration packets

Example:

```text
Input: paper_draft.md
Output: Top-10 nearest accepted papers and the main structural differences
```

That is useful because it supports revision, not because it pretends to know the
future editorial decision.

## Cram-School Risk

There is a shallow version of this idea:

```text
study what reviewers like -> imitate accepted papers -> raise acceptance odds
```

That is cram-school submission engineering.

Its behaviors are:

- copying accepted-paper format
- guessing reviewer preferences
- applying fixed templates
- optimizing for acceptance probability
- asking "will reviewers like this?" before asking "is this true and important?"

This is dangerous because it can slowly remove the research soul from the work.

The better version is not reviewer appeasement. It is scientific ecosystem
awareness.

## Deeper Version: Scientific Ecosystem Awareness

The deeper question is:

```text
How does this scientific community decide what counts as credible knowledge?
```

That opens stronger questions:

- Why are some ideas accepted and others resisted?
- Which evidence types count as trustworthy here?
- Which claims are considered overreach?
- Which uncertainty does this community try hardest to reduce?
- Which important problems are invisible because they do not fit the reviewer
  mental model?
- Does the accepted literature contain a structural blind spot?

Scientific writing is not only formal English. It is a trust-building protocol.

Limitation sections, threat models, conservative wording, reproducibility
details, ablation studies, failure analysis, and evidence traceability all help
reduce collective uncertainty.

So the best use of this system is not:

```text
How do I make this look like an accepted paper?
```

It is:

```text
What does this community currently trust, fear, reward, and fail to see?
```

That makes the idea closer to:

- meta-research
- scientometrics
- sociology of science
- philosophy of science
- computational analysis of scientific culture
- reviewer ecosystem modeling

## Working Name

`AI-assisted scientific publishing intelligence` is not a standard term yet.

Working definition:

```text
A human-AI workflow for extracting actionable submission strategy and scientific
ecosystem insight from accepted papers, journal guidelines, citation networks,
evidence standards, and reviewer-risk patterns.
```

Natural Chinese names:

- AI 輔助科學出版情報分析
- 期刊投稿情報系統
- 期刊文化反推系統
- reviewer ecosystem modeling
- acceptance pattern intelligence
