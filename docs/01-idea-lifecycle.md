# Idea Lifecycle

The lifecycle separates maturity from operations.

```text
raw -> emerging -> structured -> research_candidate -> execution_ready
```

`maturity_level` is derived from the 100-point maturity score. `status` is an
operational field and can also be `executing` or `archived`.

| Maturity Score | Level | Default Folder |
| --- | --- | --- |
| 0-20/100 | `raw` | `ideas/raw/` |
| 21-40/100 | `emerging` | `ideas/evolving/` |
| 41-60/100 | `structured` | `ideas/structured/` |
| 61-80/100 | `research_candidate` | `ideas/structured/` |
| 81-100/100 | `execution_ready` | `ideas/structured/` |

Terminal operational states:

| Status | Folder |
| --- | --- |
| `executing` | `ideas/executing/` |
| `archived` | `ideas/archived/` |
