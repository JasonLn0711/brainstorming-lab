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
