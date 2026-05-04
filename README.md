# brainstorming-lab

`brainstorming-lab` is a CLI-first Idea Operating System beside
`planning-everything-track`.

It turns loose thinking into computable idea records:

```text
raw ideas -> structured ideas -> clusters -> research candidates -> execution bridge -> feedback -> improved ideas
```

## First Principle

Ideas are data, not only text.

Each serious idea is a YAML record with score, status, tags, links, maturity,
next tests, and source. Markdown remains useful for explanation, but YAML is the
canonical database.

## Repo Roles

```text
planning-everything-track = brain / center / priorities / capacity / status / links
brainstorming-lab = idea database / critique / clustering / research generation
new project repo = execution after an idea becomes real
```

Planning receives only short bridge notes. Detailed thinking stays here.

## Folder Map

| Path | Purpose |
| --- | --- |
| `ideas/raw/` | New low-maturity ideas |
| `ideas/evolving/` | Emerging ideas that need more tests |
| `ideas/structured/` | Structured and research-ready YAML ideas |
| `ideas/executing/` | Ideas temporarily connected to execution |
| `ideas/archived/` | Closed, killed, or superseded ideas |
| `idea_os/` | Shared Python core |
| `scripts/` | CLI commands |
| `graph/` | Relationship graph builder and JSON output |
| `clustering/` | Cluster builder and YAML output |
| `research/` | Research candidate and weekly selection outputs |
| `index/` | Generated Markdown indexes |
| `schemas/` | Human-readable schema contracts |
| `docs/` | Operating documentation |
| `projects-ready/` | Compatibility layer for graduation packets |
| `archive/legacy-markdown/` | Pre-Idea-OS Markdown sources |

## Core Commands

```bash
python3 scripts/new_idea.py "New idea" --tags ai,workflow
python3 scripts/score_idea.py --all
python3 graph/build_graph.py
python3 clustering/auto_cluster.py
python3 research/generate_candidates.py
python3 scripts/generate_index.py
python3 scripts/weekly_review.py --dry-run
python3 scripts/weekly_review.py
python3 scripts/push_to_planning.py --dry-run
python3 scripts/suggest_today_ideas.py --dry-run
```

Run the full verification suite with:

```bash
python3 -m unittest
```

## Start Here

1. Read `AGENTS.md`.
2. Read `docs/system_design.md`.
3. Use `docs/usage.md` for CLI commands.
4. Inspect `index/idea_index.md` for the current idea database.
