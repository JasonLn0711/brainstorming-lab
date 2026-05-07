#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from idea_os.clustering_engine import build_clusters
from idea_os.config import load_config
from idea_os.store import REPO_ROOT, load_all_ideas
from idea_os.yaml_io import save_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Run dependency-free token-vector idea clustering.")
    parser.add_argument("--threshold", type=float, default=None)
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    repo = Path(args.root).resolve() if args.root is not None else REPO_ROOT
    config = load_config(repo)
    threshold = float(args.threshold if args.threshold is not None else config["similarity_threshold"])
    clusters = build_clusters(load_all_ideas(repo), threshold)
    output = repo / "clustering" / "clusters.yaml"
    save_yaml(output, clusters)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
