# Idea Lifecycle

## Status Rules

| Score | Status | Folder |
| ---: | --- | --- |
| 0-5 | `raw` | `ideas/raw/` |
| 6-10 | `emerging` | `ideas/evolving/` |
| 11-15 | `structured` | `ideas/structured/` |
| 16-20 | `research_ready` | `ideas/structured/` |

Manual lifecycle states:

| Status | Folder | Meaning |
| --- | --- | --- |
| `executing` | `ideas/executing/` | A bounded execution path exists |
| `archived` | `ideas/archived/` | The idea is killed, parked indefinitely, or superseded |

## Maturity Score

```text
score = clarity + testability + connectedness + evidence
```

Each maturity field is an integer from 0 to 5.

## Graduation

An idea graduates only when it has a real next output, audience or owner,
boundary, and target repo. Keep the graduation packet in `projects-ready/` until
the standalone execution repo exists.

## Stop Conditions

Archive or park when the idea duplicates existing work, fails a core assumption,
has no next test after repeated sessions, or would create maintenance without a
clear output.
