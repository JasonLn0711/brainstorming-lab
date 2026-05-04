#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from idea_os.clustering_engine import build_clusters  # noqa: E402
from idea_os.config import load_config  # noqa: E402
from idea_os.research_engine import generate_research_candidates  # noqa: E402
from idea_os.store import load_all_ideas  # noqa: E402
from idea_os.yaml_io import load_yaml, save_yaml  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate research candidates from Idea OS clusters.")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    repo = Path(args.root).resolve() if args.root is not None else ROOT
    cluster_path = repo / "clustering" / "clusters.yaml"
    ideas = load_all_ideas(repo)
    if cluster_path.exists():
        loaded = load_yaml(cluster_path)
        clusters = loaded if isinstance(loaded, dict) else {}
    else:
        config = load_config(repo)
        clusters = build_clusters(ideas, float(config["similarity_threshold"]))
    candidates = generate_research_candidates(clusters, ideas)
    output = repo / "research" / "candidates.yaml"
    save_yaml(output, candidates)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
