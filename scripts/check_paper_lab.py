#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.paper_lab import paper_folders, validate_paper_lab


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Weekly Paper Lab folders and paper.yaml records.")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    errors = validate_paper_lab(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"weekly-paper-lab OK: paper_folders={len(paper_folders(args.root))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
