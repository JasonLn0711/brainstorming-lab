#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.paper_shortlist import shortlist_paths, validate_shortlists


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate auditable Weekly Paper Lab shortlists.")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    errors = validate_shortlists(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"paper shortlists OK: files={len(shortlist_paths(args.root))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
