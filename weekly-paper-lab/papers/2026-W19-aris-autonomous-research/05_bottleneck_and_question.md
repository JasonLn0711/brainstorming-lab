# Bottleneck And Question

## Failure Log

| Type | Observation | Evidence | Next Check |
| --- | --- | --- | --- |
| engineering | Full official workflow should not be run yet because it depends on CLI/MCP/provider setup | README and `AGENT_GUIDE.md` inspected in the cloned ARIS source | Keep using bounded local fixture until provider setup is explicit |
| data | No real research evidence was used first | Synthetic fixture created under external artifact root | Add one harder negative and one insufficient-evidence claim |
| evaluation | Local fixture produced measurable unsupported-success metrics | `fixture/audit_result.yaml` | Replace manual adversarial verdicts with a local or cross-model reviewer |
| theory | Cross-model/adversarial review improved unsupported-claim detection in the toy fixture, but reviewer burden is not yet optimized | Baseline detection 0.0; adversarial detection 1.0; revision count 2 | Compare detection gain against time and revision count across larger fixtures |
| hardware | Full workflow may not need RTX 5080 | Planned Level 2 fixture | Only use local GPU if running a local reviewer model |
| environment | Credentials and API calls may be required by official workflow | ARIS docs describe Claude/Codex/reviewer provider routing and MCP setup | Do not run full ARIS workflow until credentials and cost policy are explicit |
| cost | API-based review could create hidden cost | Full workflow stopped; CPU/local-file fixture completed | Keep next run local unless a specific provider budget is approved |
| problem_definition | Need to avoid "build ARIS" as the goal | Run 001 measured claim-ledger acceptance behavior instead | Define acceptance-gate research question around claim support and reviewer burden |

## Bottleneck

The key bottleneck is not installation. It is defining a minimal, measurable
audit task that preserves the paper's research insight without turning the week
into a full autonomous-agent deployment.

After Run 001, the bottleneck is sharper: the fixture can measure whether a
review gate catches unsupported claims, but it does not yet measure whether the
reviewer is independent, scalable, or worth its burden.

## Reframed Research Question

Can Idea OS use claim-ledger review as a lightweight acceptance gate for
research-agent outputs, reducing unsupported-success errors while keeping manual
review effort low?

Run 001 version:

Can a claim-ledger gate improve unsupported-claim detection from a self-accepting
baseline without creating too many revision demands per accepted research-agent
output?

## Reading Pass 001 Critique

The paper is strongest as a systems and method report. It gives a concrete
language for the problem we care about: unsupported success, reviewer
independence, claim ledgers, and evidence-aware acceptance gates.

The paper is weaker as proof that cross-family review is causally better. Its
deployment evidence is explicitly observational, and the controlled comparison
is left as future work. That is not a fatal flaw for our use case, but it
changes how we should use it:

- Use ARIS as a method reference and failure taxonomy, not as a solved benchmark.
- Measure our own smallest acceptance-gate behavior before adopting any full
  orchestration stack.
- Treat reviewer burden as a first-class metric, because more review can improve
  detection while still being too expensive for weekly research practice.
- Keep confidential or sensitive repositories away from repository-level remote
  reviewer access unless a local-only route is explicitly approved.

Updated bottleneck: the next hard question is not "can we run ARIS?" It is
whether a five-claim fixture can separate three cases cleanly: supported,
overstated, and insufficient-evidence claims.
