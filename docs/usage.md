# CLI Usage

Run commands from the repo root.

## Create

```bash
python3 scripts/new_idea.py "AI intake triage" --type project --tags healthcare,ai-triage
```

## Scientific Pipeline

```bash
python3 scripts/normalize_problem.py
python3 scripts/score_maturity.py
python3 scripts/detect_merge_candidates.py
python3 scripts/generate_clusters.py
python3 scripts/generate_research_candidates.py
python3 scripts/generate_research_brief.py
python3 scripts/generate_index.py
```

`score_idea.py` remains as a command wrapper for `score_maturity.py`; it does
not use the retired compact score.

## Link And Status

```bash
python3 scripts/link_ideas.py idea_000001 idea_000002
python3 scripts/update_status.py idea_000001 archived
```

Mutating idea-YAML scripts create timestamped backups under
`backups/idea_yaml/`.

## Weekly Loop

```bash
python3 scripts/weekly_review.py --dry-run
python3 scripts/weekly_review.py
python3 scripts/push_to_planning.py --dry-run
python3 scripts/push_to_planning.py
```

The weekly selector uses 100-point maturity ratio, novelty, value, execution
cost, and priority-tag alignment. The output is `research/weekly_selection.yaml`.

## Daily Feedback

Daily feedback must be explicit:

```markdown
<!-- IDEA_OS_FEEDBACK_START -->
idea_000001:
  insight: "The review packet must include uncertainty labels."
  status: structured
<!-- IDEA_OS_FEEDBACK_END -->
```

Then run:

```bash
python3 scripts/pull_feedback.py --week 2026-W19 --dry-run
python3 scripts/pull_feedback.py --week 2026-W19
```
