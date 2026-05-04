#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.models import STATUSES, validate_idea
from idea_os.store import find_idea_path, load_idea, save_and_move_idea


def main() -> int:
    parser = argparse.ArgumentParser(description="Update an idea status and move it to the matching folder.")
    parser.add_argument("idea", help="Idea ID or path")
    parser.add_argument("status", choices=sorted(STATUSES))
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    path = find_idea_path(args.idea, args.root)
    idea = load_idea(path)
    idea["status"] = args.status
    errors = validate_idea(idea)
    if errors:
        raise SystemExit("; ".join(errors))
    target = save_and_move_idea(idea, path, args.root)
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
