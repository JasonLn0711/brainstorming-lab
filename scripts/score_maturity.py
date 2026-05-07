#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime

import _bootstrap  # noqa: F401
from idea_os.models import score_idea, validate_idea
from idea_os.store import find_idea_path, iter_active_idea_files, load_active_ideas, load_idea, save_and_move_idea


def score_path(path, all_ideas, root=None, backup_run_id=None) -> tuple[str, str, str, str]:
    idea = load_idea(path)
    score_idea(idea, all_ideas=all_ideas)
    errors = validate_idea(idea)
    if errors:
        raise ValueError(f"{idea.get('id', path)}: " + "; ".join(errors))
    target = save_and_move_idea(idea, path, root, backup=True, backup_run_id=backup_run_id)
    return idea["id"], idea["maturity_score"], idea["maturity_level"], str(target)


def main() -> int:
    parser = argparse.ArgumentParser(description="Recalculate 100-point Idea OS maturity score and level.")
    parser.add_argument("target", nargs="?", help="Idea ID or path; defaults to all active ideas")
    parser.add_argument("--all", action="store_true", help="Score all active ideas")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    paths = [find_idea_path(args.target, args.root)] if args.target else iter_active_idea_files(args.root)
    all_ideas = load_active_ideas(args.root)
    run_id = datetime.now().strftime("%Y%m%dT%H%M%S")
    changed = 0
    failures = 0
    for path in paths:
        try:
            idea_id, score, level, target = score_path(path, all_ideas, args.root, run_id)
        except Exception as exc:
            failures += 1
            print(f"ERROR {path}: {exc}")
            continue
        changed += 1
        print(f"{idea_id}: maturity_score={score} maturity_level={level} path={target}")
    print(f"scored={changed} failed={failures} backup_run={run_id}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
