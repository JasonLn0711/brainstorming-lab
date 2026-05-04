#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.models import score_idea, validate_idea
from idea_os.store import find_idea_path, iter_idea_files, load_idea, save_and_move_idea


def score_path(path, root=None) -> tuple[str, int, str]:
    idea = load_idea(path)
    score_idea(idea)
    errors = validate_idea(idea)
    if errors:
        raise ValueError(f"{idea.get('id', path)}: " + "; ".join(errors))
    new_path = save_and_move_idea(idea, path, root)
    return idea["id"], idea["score"], str(new_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Recalculate Idea OS maturity score and status.")
    parser.add_argument("target", nargs="?", help="Idea ID or path")
    parser.add_argument("--all", action="store_true", help="Score all ideas")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    if not args.all and not args.target:
        parser.error("provide an idea target or --all")

    paths = iter_idea_files(args.root) if args.all else [find_idea_path(args.target, args.root)]
    for path in paths:
        idea_id, score, new_path = score_path(path, args.root)
        print(f"{idea_id}: score={score} path={new_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
