#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from idea_os.research_engine import generate_research_candidates, write_research_briefs
from idea_os.clustering_engine import build_clusters
from idea_os.store import load_active_ideas
from idea_os.yaml_io import load_yaml, save_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Markdown research briefs from research candidates.")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    repo = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    candidate_path = repo / "research" / "research_candidates.yaml"
    if candidate_path.exists():
        loaded = load_yaml(candidate_path)
        candidates = loaded if isinstance(loaded, dict) else {}
    else:
        ideas = load_active_ideas(repo)
        clusters = build_clusters(ideas, 60)
        save_yaml(repo / "clusters" / "active_clusters.yaml", clusters)
        candidates = generate_research_candidates(clusters, ideas)
        save_yaml(candidate_path, candidates)
    paths = write_research_briefs(candidates, repo)
    print(f"{repo / 'research' / 'research_briefs'} briefs={len(paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
