#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from idea_os.paper_quality import blank_quality_evaluation
from idea_os.store import REPO_ROOT
from idea_os.yaml_io import load_yaml, save_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a blank scientific_evaluation.yaml for a paper folder.")
    parser.add_argument("paper_folder", help="Path to weekly-paper-lab/papers/<YYYY-Www-slug>")
    parser.add_argument("--paper-type", default="system_paper", help="Paper type label, for example system_paper")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing scientific_evaluation.yaml")
    args = parser.parse_args()

    paper_dir = Path(args.paper_folder)
    if not paper_dir.is_absolute():
        paper_dir = REPO_ROOT / paper_dir
    paper_yaml = paper_dir / "paper.yaml"
    if not paper_yaml.exists():
        print(f"ERROR: missing {paper_yaml}")
        return 1

    output = paper_dir / "scientific_evaluation.yaml"
    if output.exists() and not args.force:
        print(f"ERROR: {output} already exists; pass --force to replace it")
        return 1

    paper_record = load_yaml(paper_yaml)
    paper_id = str(paper_record.get("paper_id", paper_dir.name))
    save_yaml(output, blank_quality_evaluation(paper_id, args.paper_type))
    print(f"created {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
