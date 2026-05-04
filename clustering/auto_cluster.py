#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from idea_os.clustering_engine import build_clusters  # noqa: E402
from idea_os.store import load_active_ideas  # noqa: E402
from idea_os.yaml_io import save_yaml  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto-cluster Idea OS YAML records.")
    parser.add_argument("--threshold", type=int, default=60)
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    repo = Path(args.root).resolve() if args.root is not None else ROOT
    clusters = build_clusters(load_active_ideas(repo), args.threshold)
    output = repo / "clusters" / "active_clusters.yaml"
    save_yaml(output, clusters)
    print(f"{output} clusters={len(clusters)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
