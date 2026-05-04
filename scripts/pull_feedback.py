#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date

import _bootstrap  # noqa: F401
from idea_os.planning import load_feedback_from_daily
from idea_os.store import find_idea_path, load_idea, save_and_move_idea


def apply_feedback(idea: dict, feedback: dict) -> None:
    if "status" in feedback and feedback["status"]:
        idea["status"] = str(feedback["status"])
    insights = idea.setdefault("insights", [])
    for key in ["insight", "insights"]:
        value = feedback.get(key)
        if not value:
            continue
        if isinstance(value, list):
            for item in value:
                if item not in insights:
                    insights.append(str(item))
        elif str(value) not in insights:
            insights.append(str(value))


def main() -> int:
    parser = argparse.ArgumentParser(description="Pull explicit Idea OS feedback markers from a planning day note.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Target date YYYY-MM-DD")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    feedback = load_feedback_from_daily(date.fromisoformat(args.date), args.root)
    for idea_id, data in feedback.items():
        if not isinstance(data, dict):
            continue
        path = find_idea_path(idea_id, args.root)
        idea = load_idea(path)
        apply_feedback(idea, data)
        target = save_and_move_idea(idea, path, args.root)
        print(f"updated {idea_id}: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
