# Problem

## Author Problem

Long-horizon research agents can produce plausible research outputs whose claims
are not fully supported by the underlying evidence. The hard failure is not only
that an agent visibly crashes; it is that it appears to succeed while quietly
misreporting, omitting, or overextending evidence.

## Why Now

Agent systems are moving from short task execution into research workflows:
literature review, experiment planning, figure generation, paper writing, and
rebuttal drafting. Once an agent chain becomes long enough, ordinary completion
signals are too weak. The workflow needs evidence-aware assurance.

## Assumptions

- Cross-role or cross-model review can catch errors that same-role self-review misses.
- Claim-to-evidence mapping is a useful minimum unit for auditing research-agent output.
- A small synthetic fixture can reveal workflow failure modes before running expensive full workflows.
- The useful first target is not autonomy itself, but unsupported-success reduction.

## Boundary

This first lab will not validate ARIS as a full research system. It will only
test whether the paper's assurance framing can be turned into a small,
repeatable Idea OS fixture.

## Reading Pass 001

The paper frames the problem more sharply than "make research agents better."
Its actual core is harness reliability: for long research workflows, the
dangerous failure mode is an artifact that looks complete while its claims are
unsupported, overstated, or inherited from the executor's framing.

For our Idea OS use, this yields three problem constraints:

- Persistent state is required because review is meaningless if evidence,
  decisions, claims, and negative outcomes disappear between sessions.
- Modular execution is required because a long research process must expose
  replaceable stages, not a single opaque agent trajectory.
- Independent assurance is required because self-review can preserve the same
  blind spot that created the unsupported claim.

The paper's own limitation matters for our reading: it reports early deployment
experience, but it does not yet establish a controlled causal comparison showing
that cross-family review beats same-family or self-review under matched cost.
That is why our local question should stay narrower: can a claim-ledger gate
produce measurable unsupported-success signals before we discuss autonomy?
