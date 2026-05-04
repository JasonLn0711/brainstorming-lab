#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from idea_os.clustering_engine import build_clusters
from idea_os.research_engine import generate_research_candidates
from idea_os.store import load_active_ideas
from idea_os.yaml_io import load_yaml, save_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate research candidates from active clusters.")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    repo = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    ideas = load_active_ideas(repo)
    cluster_path = repo / "clusters" / "active_clusters.yaml"
    if cluster_path.exists():
        loaded = load_yaml(cluster_path)
        clusters = loaded if isinstance(loaded, dict) else {}
    else:
        clusters = build_clusters(ideas, 60)
        save_yaml(cluster_path, clusters)
    candidates = generate_research_candidates(clusters, ideas)
    output = repo / "research" / "research_candidates.yaml"
    save_yaml(output, candidates)
    print(f"{output} candidates={len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
