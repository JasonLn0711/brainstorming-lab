#!/usr/bin/env python3
from __future__ import annotations

import argparse

import _bootstrap  # noqa: F401
from idea_os.store import make_template_idea, next_idea_id, path_for_idea, save_idea


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new Idea OS YAML record.")
    parser.add_argument("title", help="Idea title")
    parser.add_argument("--type", default="concept", choices=["concept", "question", "hypothesis", "project"])
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--date", default=None, help="Creation date YYYY-MM-DD")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    idea = make_template_idea(next_idea_id(args.root), args.title, args.type, tags, args.date)
    path = path_for_idea(idea, args.root)
    save_idea(path, idea)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
