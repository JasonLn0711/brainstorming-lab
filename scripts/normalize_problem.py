#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime

import _bootstrap  # noqa: F401
from idea_os.models import score_idea, validate_idea
from idea_os.problem import normalize_idea_problem
from idea_os.store import find_idea_path, iter_active_idea_files, load_idea, save_and_move_idea


def normalize_path(path, root=None, backup_run_id=None) -> tuple[str, str, str]:
    idea = load_idea(path)
    normalize_idea_problem(idea)
    score_idea(idea)
    errors = validate_idea(idea)
    if errors:
        raise ValueError(f"{idea.get('id', path)}: " + "; ".join(errors))
    target = save_and_move_idea(idea, path, root, backup=True, backup_run_id=backup_run_id)
    return idea["id"], idea.get("normalization_status", ""), str(target)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize idea problem statements with deterministic templates.")
    parser.add_argument("target", nargs="?", help="Idea ID or path; defaults to all active ideas")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    paths = [find_idea_path(args.target, args.root)] if args.target else iter_active_idea_files(args.root)
    run_id = datetime.now().strftime("%Y%m%dT%H%M%S")
    changed = 0
    failures = 0
    for path in paths:
        try:
            idea_id, status, target = normalize_path(path, args.root, run_id)
        except Exception as exc:
            failures += 1
            print(f"ERROR {path}: {exc}")
            continue
        changed += 1
        print(f"{idea_id}: normalization_status={status} path={target}")
    print(f"normalized={changed} failed={failures} backup_run={run_id}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
