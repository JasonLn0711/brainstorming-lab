# Key Figures

## Figure Or Table Inventory

| Figure/Table | Claim | What To Check |
| --- | --- | --- |
| ARIS architecture | Research agents need executor, orchestration, and assurance layers | Can the layers map to a tiny local fixture? |
| Evidence-to-claim audit | Unsupported claims can be caught by explicit mapping | Can we score claim support without full ARIS? |
| Self-improvement loop | Workflow improvements need reviewer approval | Can Idea OS feedback markers play the same role? |

## Reading Pass 001 Figure Notes

| Paper element | First-pass reading | Local translation |
| --- | --- | --- |
| Workflow library | Five workflows cover discovery, experiment bridge, auto-review, paper writing, and rebuttal. | Do not copy the full stack; keep W19 to paper reading plus one fixture. |
| Auto-review loop | Reviewer score, action items, optional experiments, revision, convergence check. | Compare baseline self-acceptance against adversarial review on fixed claims. |
| Paper-writing pipeline | Claim audit, proof check, citation audit, visual PDF review sit inside manuscript production. | Use only the claim-audit idea first; manuscript automation is out of scope. |
| System topology | Skills, workflows, artifacts, assurance, model/tool bridges, and meta-optimization are separated. | Useful architecture reference for `idea_000008`, but not an implementation target this week. |
| Evidence-to-claim cascade | Experiment audit -> result-to-claim -> paper-claim audit. | Our fixture should keep separate files for claims, evidence, reviewer verdicts, and audit result. |
| Controlled benchmark appendix | Proposed future benchmark compares self-critique, same-model agents, cross-model, reversed cross-model, and same-model-for-second-model conditions. | This is the stronger future research shape for Idea OS: matched cost, issue recall, false positives, actionability, quality, cost, and latency. |

## Reconstructed Diagram

```text
research task
  -> executor produces artifact
  -> claim ledger extracts claims
  -> reviewer checks claims against evidence
  -> revision request or approval
  -> accepted insight updates research memory or Idea OS
```

## Evidence Strength

The strongest claim for our purposes is the assurance layer: if claims can be
mapped to evidence before acceptance, then autonomous research workflows become
more inspectable and less likely to hide unsupported success.
