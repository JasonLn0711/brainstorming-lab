# Start Here

Use this repo when an idea needs more thinking room than a daily note.

## Quick Routing

| Situation | Action |
| --- | --- |
| One passing thought | Keep one line in the planning day note |
| Idea needs structure | Create a YAML record with `scripts/new_idea.py` |
| Idea needs repeated sessions | Keep updating the YAML record and supporting docs here |
| Idea may become a project | Create `projects-ready/YYYY-MM-DD-project-slug.md` |
| Idea may become a paper | Use `docs/paper-writing-engineering-process.md` before drafting |
| Personal/admin record needs structured retrieval | Keep a redacted summary in `docs/personal-admin/`; keep raw private files in `~/system-hub/admin/inventory/`; sync only deadline/status to planning |
| Project is real | Move execution into a new standalone repo |
| Lesson is reusable | Promote a distilled note into `planning-everything-track/data/knowledge/` |

## Minimum Idea Record

Every YAML idea should answer:

- What problem does it address?
- Why might it matter?
- What assumptions might fail?
- How mature is it?
- Which ideas is it connected to?
- What is the smallest next test?

## First Commands

```bash
python3 scripts/normalize_problem.py
python3 scripts/score_maturity.py
python3 scripts/generate_index.py
```

Then inspect:

```text
index/idea_index.md
index/tag_index.md
```

## Paper Writing

Before drafting or revising a manuscript, write:

- one-sentence claim
- reviewer question list
- contribution-to-evidence map
- Figure 1 overview
- main-text vs appendix split

Use `docs/paper-writing-engineering-process.md` as the canonical writing
process.

## Planning Bridge

The planning repo should keep only:

- one-line summary
- canonical idea path
- next test
- capacity impact
- project locator after graduation
