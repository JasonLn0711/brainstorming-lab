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
