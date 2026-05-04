# CLI Usage

Run commands from the repo root.

## Create

```bash
python3 scripts/new_idea.py "AI intake triage" --type project --tags healthcare,ai-triage
```

## Score

```bash
python3 scripts/score_idea.py idea_000001
python3 scripts/score_idea.py --all
```

## Link

```bash
python3 scripts/link_ideas.py idea_000001 idea_000002
```

## Status

```bash
python3 scripts/update_status.py idea_000001 archived
```

## Generate Artifacts

```bash
python3 graph/build_graph.py
python3 clustering/auto_cluster.py
python3 research/generate_candidates.py
python3 scripts/generate_index.py
```

## Weekly Loop

```bash
python3 scripts/weekly_review.py
python3 scripts/push_to_planning.py --dry-run
python3 scripts/push_to_planning.py
```

## Daily Loop

```bash
python3 scripts/suggest_today_ideas.py --dry-run
python3 scripts/suggest_today_ideas.py
```

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
python3 scripts/pull_feedback.py
```
