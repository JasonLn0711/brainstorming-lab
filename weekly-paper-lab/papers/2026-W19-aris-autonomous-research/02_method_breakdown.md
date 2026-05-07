# Method Breakdown

## Core Method

1. Use an executor role to advance a research workflow.
2. Use a reviewer role, ideally from a different model family or reasoning style, to critique intermediate artifacts.
3. Keep a persistent research memory or wiki so prior work can be reused.
4. Map experimental results and manuscript claims into an auditable ledger.
5. Run assurance passes that check whether claims are supported by the ledger and raw evidence.
6. Adopt self-improvement proposals only after review.

## Inputs And Outputs

- Inputs: research direction, paper or code references, intermediate artifacts, evidence snippets, claim ledger.
- Outputs: revised research artifacts, claim-support judgments, reviewer requests, final report or manuscript material.

## Baselines

- Single-agent self-review.
- Manual review without a claim ledger.
- Same-model executor and reviewer.

## Evaluation

- Claim-to-evidence mapping rate.
- Unsupported-claim detection rate.
- Number of reviewer-requested revisions.
- Manual inspection time.
- Whether the final artifact overclaims less than the baseline.

## Rebuild Plan

Build a three-claim synthetic fixture:

1. One claim fully supported by evidence.
2. One claim partially supported but overstated.
3. One claim unsupported but plausible.

Then compare a baseline self-review against a simple adversarial reviewer pass.

## Reading Pass 001

The reusable method can be decomposed into a small local protocol:

1. Executor produces a bounded artifact and a claim list.
2. Evidence is stored separately from the artifact, with enough structure to
   let a reviewer inspect it directly.
3. A claim ledger assigns each claim a support state: supported, partial, or
   invalidated.
4. A fresh reviewer checks the artifact against the ledger and raw evidence,
   preferably without receiving the executor's summary first.
5. The system accepts, revises, or abstains based on evidence support and
   reviewer burden, not on whether the artifact sounds polished.

The paper has a larger stack around this: workflow orchestration, reusable
Markdown skills, a research wiki, manuscript checks, proof checks, citation
audit, visual PDF review, and meta-optimization. For this lab, those are
secondary. The direct method reference is the evidence-to-claim audit cascade
and the reviewer-independence protocol.

The next method question is whether the reviewer must be a frontier remote model
or whether a local reviewer model can catch the same hard negatives in a small
fixture. That keeps the test aligned with the paper while respecting our cost,
credential, and repo-boundary rules.
