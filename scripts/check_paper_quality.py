#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.paper_quality import quality_evaluation_files, validate_quality_evaluation_file


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Scientific Paper Evaluation records.")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    errors: list[str] = []
    files = quality_evaluation_files(args.root)
    for path in files:
        errors.extend(validate_quality_evaluation_file(path, args.root))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"scientific paper evaluations OK: files={len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
