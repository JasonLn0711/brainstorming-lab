# Ideas

Idea YAML files are the canonical database.

| Folder | Status values |
| --- | --- |
| `raw/` | `raw` |
| `evolving/` | `emerging` |
| `structured/` | `structured`, `research_candidate`, `execution_ready` |
| `executing/` | `executing` |
| `archived/` | `archived` |

Use:

```bash
python3 scripts/new_idea.py "Idea title" --tags tag1,tag2
python3 scripts/normalize_problem.py
python3 scripts/score_maturity.py
python3 scripts/link_ideas.py idea_000001 idea_000002
```

Current generated overview:

```text
index/idea_index.md
index/tag_index.md
index/cluster_index.md
index/research_candidate_index.md
```
