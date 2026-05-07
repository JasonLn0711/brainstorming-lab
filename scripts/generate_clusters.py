#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from idea_os.clustering_engine import build_clusters
from idea_os.store import load_active_ideas
from idea_os.yaml_io import save_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate active research clusters from merge scores.")
    parser.add_argument("--threshold", type=int, default=60, help="Minimum merge score for cluster edges")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    repo = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    clusters = build_clusters(load_active_ideas(repo), args.threshold)
    output = repo / "clusters" / "active_clusters.yaml"
    save_yaml(output, clusters)
    print(f"{output} clusters={len(clusters)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
