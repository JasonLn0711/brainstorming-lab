#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from idea_os.merge import detect_merge_candidates
from idea_os.store import load_active_ideas
from idea_os.yaml_io import save_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect duplicate, cluster, and synthesis candidates.")
    parser.add_argument("--min-score", type=int, default=40, help="Minimum merge score to include")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    repo = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    ideas = load_active_ideas(repo)
    candidates = detect_merge_candidates(ideas, args.min_score)
    output = repo / "clusters" / "merge_candidates.yaml"
    save_yaml(output, candidates)
    print(f"{output} candidates={len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
