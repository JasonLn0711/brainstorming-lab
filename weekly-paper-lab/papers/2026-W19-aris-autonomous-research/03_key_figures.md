# Key Figures

## Figure Or Table Inventory

| Figure/Table | Claim | What To Check |
| --- | --- | --- |
| ARIS architecture | Research agents need executor, orchestration, and assurance layers | Can the layers map to a tiny local fixture? |
| Evidence-to-claim audit | Unsupported claims can be caught by explicit mapping | Can we score claim support without full ARIS? |
| Self-improvement loop | Workflow improvements need reviewer approval | Can Idea OS feedback markers play the same role? |

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
