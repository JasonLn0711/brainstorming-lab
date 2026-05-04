#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import _bootstrap  # noqa: F401
from idea_os.config import load_config
from idea_os.planning import iso_week_folder
from idea_os.store import REPO_ROOT, load_all_ideas
from idea_os.yaml_io import save_yaml


def build_selection(root=None, threshold=12, top_n=None) -> dict:
    config = load_config(root)
    limit = int(top_n or config.get("top_n", 3))
    ideas = [
        idea
        for idea in load_all_ideas(root)
        if int(idea.get("score", 0)) >= threshold and idea.get("status") != "archived"
    ]
    ideas.sort(key=lambda item: (-int(item.get("score", 0)), item["id"]))
    selection = {
        "week": iso_week_folder(date.today()),
        "threshold": threshold,
        "top_n": limit,
    }
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    for index, idea in enumerate(ideas[:limit], start=1):
        steps = idea.get("next_steps", [])
        selection[f"selection_{index:03d}"] = {
            "id": idea["id"],
            "title": idea.get("title", ""),
            "status": idea.get("status", ""),
            "score": idea.get("score", 0),
            "next_step": steps[0] if steps else "",
            "path": str(Path(idea.get("_path", "")).resolve().relative_to(repo))
            if idea.get("_path")
            else "",
        }
    return selection


def main() -> int:
    parser = argparse.ArgumentParser(description="Select top Idea OS ideas for weekly review.")
    parser.add_argument("--threshold", type=int, default=12)
    parser.add_argument("--top-n", type=int, default=None)
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    selection = build_selection(args.root, args.threshold, args.top_n)
    repo = Path(args.root).resolve() if args.root is not None else REPO_ROOT
    output = repo / "research" / "weekly_selection.yaml"
    save_yaml(output, selection)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
