# Research Idea Seed

## Candidate Question

Can a lightweight cross-role evidence-audit loop reduce unsupported-success
errors in small research-agent workflows without increasing reviewer burden too
much?

## Possible Contribution

A bounded benchmark fixture for research-agent assurance:

- synthetic claims
- evidence snippets
- baseline self-review
- adversarial reviewer pass
- claim-support score
- reviewer-burden score

## Synthesis Assessment

- Score: 20/20 under `paper_synthesis_rubric_v1`
- Reference role: method reference
- Combine with: `idea_000008`, `idea_000007`, `idea_000006`
- Candidate method: claim-ledger-guided adversarial review for small research-agent workflows.
- Idea connection scores under `paper_connection_rubric_v2`:
  - `idea_000008`: 100/100
  - `idea_000007`: 93/100
  - `idea_000006`: 50/100

## Idea OS Action

- update_idea: `idea_000008`
- possible link: `idea_000007`
- possible link: `idea_000006`

## Next Test

Create the local synthetic fixture under:

```text
/home/jnln3799/research-artifacts/weekly-paper-lab/2026-W19-aris-autonomous-research/
```

Run 001 completed the local synthetic fixture. Next, add a second fixture with at
least five claims:

- one supported claim
- two unsupported or overstated claims
- one partial claim
- one insufficient-evidence claim

Then compare manual adversarial review against a local or cross-model reviewer
while keeping the same audit schema.

## Reading Pass 001 Hypothesis Update

The paper's most reusable idea for `idea_000008` is not multi-agent automation
itself. It is a conductor acceptance rule:

```text
accept only when claim support is explicit enough, reviewer objections are
resolved or bounded, and the extra review cost is justified by risk reduction
```

That points to a small research contribution:

- define a claim-ledger schema for research-agent outputs;
- compare self-review, same-role review, and independent adversarial review;
- measure unsupported-claim detection, false positives, revision count, review
  time, and accept/abstain quality;
- use the result as a workflow-depth signal for the learned-conductor idea.

This keeps the future project centered on orchestration policy rather than
copying ARIS's whole skill ecosystem.

## Problem-Definition Link

The reading pass also updates `idea_000012`: ARIS is a good training case for
separating a tool-shaped impulse from the actual research problem.

Tool-shaped impulse:

```text
run a full autonomous research-agent stack
```

First-principles bottleneck:

```text
research-agent outputs can look successful while unsupported claims survive
unless evidence support, reviewer independence, and acceptance cost are made
measurable
```

That means the next research seed should be evaluated as a problem-definition
exercise before it becomes implementation work. The five-claim fixture should
ask whether the bottleneck is evidence mapping, reviewer independence, revision
burden, or unclear acceptance criteria.

## Run 001 Result

- Run ID: `2026-W19-aris-claim-ledger-fixture-001`
- Artifact: `/home/jnln3799/research-artifacts/weekly-paper-lab/2026-W19-aris-autonomous-research/fixture/audit_result.yaml`
- Claim count: 3
- Claim-to-evidence mapping rate: 1.0
- Baseline unsupported-claim detection rate: 0.0
- Adversarial unsupported-claim detection rate: 1.0
- Reviewer revision count: 2
- Manual inspection time: 18 minutes

Interpretation: the fixture supports the research seed. A self-accepting
baseline missed the unsupported quantifier claim, while adversarial review caught
it and also forced one partial claim to be qualified. This is not evidence that
ARIS works end to end; it is evidence that a claim-ledger gate can produce
measurable acceptance/revision signals.

## Links

- Idea OS YAML: `ideas/structured/idea_000008_learned_conductor_for_medical_ai_research_workflows.yaml`
- Idea OS YAML: `ideas/structured/idea_000007_signal_market_for_low_cost_behavior_discovery.yaml`
- Idea OS YAML: `ideas/structured/idea_000006_openclaw_personal_ops_node.yaml`
- Idea OS YAML: `ideas/structured/idea_000012_phd_problem_definition_thinking_system.yaml`
- Planning note: synced in `planning-everything-track/weeks/2026-W19/days/2026-05-07.md`
