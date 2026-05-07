#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.indexer import generate_indexes
from idea_os.store import load_all_ideas


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate markdown Idea OS indexes.")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    paths = generate_indexes(load_all_ideas(args.root), args.root)
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
