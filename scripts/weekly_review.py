#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import _bootstrap  # noqa: F401
from idea_os.planning import iso_week_folder
from idea_os.selection import build_weekly_selection
from idea_os.store import REPO_ROOT
from idea_os.yaml_io import dumps_yaml, save_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Run adaptive Idea OS weekly selection.")
    parser.add_argument("--top-n", type=int, default=None)
    parser.add_argument("--week", default=iso_week_folder(date.today()), help="ISO week, e.g. 2026-W19")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    selection = build_weekly_selection(args.root, args.week, args.top_n)
    if args.dry_run:
        print(dumps_yaml(selection))
        return 0
    repo = Path(args.root).resolve() if args.root is not None else REPO_ROOT
    output = repo / "research" / "weekly_selection.yaml"
    save_yaml(output, selection)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
