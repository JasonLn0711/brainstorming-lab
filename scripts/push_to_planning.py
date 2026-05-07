#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.planning import read_weekly_selection, render_weekly_bridge, write_weekly_bridge


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a short Idea OS weekly bridge into planning.")
    parser.add_argument("--dry-run", action="store_true", help="Print output instead of writing")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    selection = read_weekly_selection(args.root)
    if args.dry_run:
        print(render_weekly_bridge(selection))
        return 0
    path = write_weekly_bridge(selection, args.root)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
