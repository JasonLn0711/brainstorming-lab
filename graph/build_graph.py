#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from idea_os.config import load_config  # noqa: E402
from idea_os.graphing import build_graph  # noqa: E402
from idea_os.store import load_all_ideas  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the Idea OS relationship graph.")
    parser.add_argument("--threshold", type=float, default=None)
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    repo = Path(args.root).resolve() if args.root is not None else ROOT
    config = load_config(repo)
    threshold = float(args.threshold if args.threshold is not None else config["similarity_threshold"])
    graph = build_graph(load_all_ideas(repo), threshold)
    output = repo / "graph" / "idea_graph.json"
    output.write_text(json.dumps(graph, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
