# brainstorming-lab

`brainstorming-lab` is a CLI-first Idea Operating System beside
`planning-everything-track`.

It turns loose thinking into computable idea records:

```text
raw ideas -> structured ideas -> clusters -> research candidates -> execution bridge -> feedback -> improved ideas
```

## First Principle

Ideas are data, not only text.

Each serious idea is a YAML record with 100-point maturity, normalized problem
statement, status, tags, links, baseline, metrics, next tests, and source.
Markdown remains useful for explanation, but YAML is the canonical database.

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
| `weekly-paper-lab/` | Weekly paper reading, RTX 5080 reproduction notes, scientific-quality scoring, and research-question seeds |
| `index/` | Generated Markdown indexes |
| `schemas/` | Human-readable schema contracts |
| `docs/` | Operating documentation |
| `projects-ready/` | Compatibility layer for graduation packets |
| `archive/legacy-markdown/` | Pre-Idea-OS Markdown sources |

## Paper Writing Process

Use `docs/paper-writing-engineering-process.md` when a brainstorm, paper-lab
reading, or active manuscript needs to become a journal-style paper. The durable
rule is: one paper protects one main problem, one main method, one main evidence
stack, and one contribution statement.

## Legacy Markdown Brainstorms

This checkout preserves local Markdown brainstorms that predate the YAML-first
Idea OS structure. Treat them as human-readable reasoning records and migrate
their status, maturity, tags, next tests, and links into YAML when they become
active Idea OS work.

- `ideas/ant-colony-pheromone-graph-search-social-simulation.md`
  - Research brainstorm connecting ant colony pheromones, stigmergy, Dijkstra, A*, traffic optimization, education resource allocation, reputation signals, scam diffusion, platform heat, and a possible pheromone-based social digital twin.
- `ideas/youtube-download-terminal-yt-dlp-ubuntu.md`
  - Technical learning and research-boundary note for Ubuntu terminal YouTube download troubleshooting with `yt-dlp`, including update recovery, Bash command cache behavior, safer format selection, and legal / ethical limits.
- `ideas/ai-aware-grid-decision-twin-power-grid-brainstorm.md`
  - Parked research prototype seed; execution material lives in `../ai-aware-grid-decision-twin/`.
- `ideas/classical-chinese-jailbreak-cross-lingual-safety-blind-spot.md`
  - Cross-lingual / cross-register LLM safety brainstorm based on arXiv `2602.22983`, updated after GPT-5.5 tests suggested simple classical / Latin-style cases may already be safely handled by current frontier models.
- `ideas/japan-local-systems-as-legacy-distributed-infrastructure-brainstorm.md`
  - Detailed local-systems brainstorm paired with a distilled durable note in the planning repo.
- `ideas/taiwan-academic-research-team-scale-structure-incentives.md`
  - Private research-system / strategy brainstorm on why foreign top papers often look like large team releases, why Taiwan research often appears more solo/lab-scoped, how lab/company boundary constraints can block academic output, and how to build a solo-safe `non-human shadow team` with public data, open models, AI-assisted critique, modular work blocks, and reproducible pipelines.
- `ideas/transformers-inherently-succinct-theory-backbone-ai-safety.md`
  - Parked theory / AI-safety brainstorm seed for transformer succinctness, representation-space compression, EXPSPACE-complete verification hardness, residual risk, bounded safety, and agent-governance invariants.
  - Use as theory support for the cross-lingual safety note, not as direct proof that every deployed LLM has an exploitable jailbreak.
- `ideas/2026-04-30-brainstorm-capture.md`
  - Date-level capture index for older brainstorm routing.

## Core Commands

Use a per-repo virtual environment on Ubuntu 24 / Debian-family systems:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-dev.txt
```

If `python3 -m venv .venv` reports that the virtual environment was not created
successfully, install the OS venv support first:

```bash
sudo apt update
sudo apt install python3-venv python3-full
python3 -m venv .venv
```

```bash
python3 scripts/new_idea.py "New idea" --tags ai,workflow
python3 scripts/normalize_problem.py
python3 scripts/score_maturity.py
python3 scripts/detect_merge_candidates.py
python3 scripts/generate_clusters.py
python3 scripts/generate_research_candidates.py
python3 scripts/generate_research_brief.py
python3 graph/build_graph.py
python3 scripts/generate_index.py
python3 scripts/check_paper_shortlist.py
python3 scripts/check_paper_lab.py
python3 scripts/check_paper_quality.py
python3 scripts/weekly_review.py --dry-run
python3 scripts/weekly_review.py
python3 scripts/push_to_planning.py --dry-run
python3 scripts/suggest_today_ideas.py --dry-run
```

Run the full verification suite with:

```bash
python3 -m unittest
pytest -q
```

## Start Here

1. Read `AGENTS.md`.
2. Read `docs/system_design.md`.
3. Use `docs/usage.md` for CLI commands.
4. Use `docs/paper-writing-engineering-process.md` for reusable manuscript
   drafting and revision rules.
5. Inspect `index/idea_index.md` for the current idea database.
