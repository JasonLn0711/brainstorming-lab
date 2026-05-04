#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.store import find_idea_path, load_idea, save_idea


def add_link(idea: dict, other_id: str) -> None:
    connections = idea.setdefault("connections", [])
    if other_id not in connections:
        connections.append(other_id)
        connections.sort()


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a bidirectional connection between two ideas.")
    parser.add_argument("left", help="First idea ID or path")
    parser.add_argument("right", help="Second idea ID or path")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    left_path = find_idea_path(args.left, args.root)
    right_path = find_idea_path(args.right, args.root)
    left = load_idea(left_path)
    right = load_idea(right_path)
    add_link(left, right["id"])
    add_link(right, left["id"])
    save_idea(left_path, left)
    save_idea(right_path, right)
    print(f"linked {left['id']} <-> {right['id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
