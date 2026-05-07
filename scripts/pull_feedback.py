#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from datetime import datetime

import _bootstrap  # noqa: F401
from idea_os.models import score_idea
from idea_os.models import LEGACY_MATURITY_ALIASES
from idea_os.planning import load_feedback_from_daily, load_feedback_from_week
from idea_os.store import find_idea_path, load_idea, save_and_move_idea
from idea_os.yaml_io import dumps_yaml


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
    experiment_result = feedback.get("experiment_result")
    if experiment_result:
        result_text = f"Experiment result: {experiment_result}"
        if result_text not in insights:
            insights.append(result_text)

    maturity_delta = feedback.get("maturity_delta")
    if isinstance(maturity_delta, dict):
        maturity = idea.setdefault("maturity", {})
        for field, delta in maturity_delta.items():
            target = LEGACY_MATURITY_ALIASES.get(str(field), str(field))
            current = int(maturity.get(target, 0))
            maturity[target] = max(0, current + int(delta))
        score_idea(idea)


def main() -> int:
    parser = argparse.ArgumentParser(description="Pull explicit Idea OS feedback markers from a planning day note.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Target date YYYY-MM-DD")
    parser.add_argument("--week", default=None, help="Target ISO week YYYY-Www; reads Monday-Friday daily notes")
    parser.add_argument("--dry-run", action="store_true", help="Print parsed feedback without updating idea YAML")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    feedback = (
        load_feedback_from_week(args.week, args.root)
        if args.week
        else load_feedback_from_daily(date.fromisoformat(args.date), args.root)
    )
    if args.dry_run:
        print(dumps_yaml(feedback))
        return 0
    run_id = datetime.now().strftime("%Y%m%dT%H%M%S")
    for idea_id, data in feedback.items():
        if not isinstance(data, dict):
            continue
        path = find_idea_path(idea_id, args.root)
        idea = load_idea(path)
        apply_feedback(idea, data)
        target = save_and_move_idea(idea, path, args.root, backup=True, backup_run_id=run_id)
        print(f"updated {idea_id}: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
