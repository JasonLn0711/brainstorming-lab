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
- Planning note: not synced
