# Idea Lifecycle

This repo now uses `docs/lifecycle.md` as the canonical lifecycle contract.

Short version:

```text
raw -> emerging -> structured -> research_ready -> executing or archived
```

The score rule is:

```text
score = clarity + testability + connectedness + evidence
```

Folders:

| Folder | Status |
| --- | --- |
| `ideas/raw/` | `raw` |
| `ideas/evolving/` | `emerging` |
| `ideas/structured/` | `structured`, `research_ready` |
| `ideas/executing/` | `executing` |
| `ideas/archived/` | `archived` |

When an idea becomes real, create a graduation packet in `projects-ready/` and
move execution material into a standalone project repo.
