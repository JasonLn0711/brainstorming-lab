#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date

import _bootstrap  # noqa: F401
from idea_os.planning import daily_note_path, insert_or_replace_block, read_weekly_selection, render_today_block, update_daily_note


def main() -> int:
    parser = argparse.ArgumentParser(description="Append selected Idea OS suggestions to a planning day note.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Target date YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--root", default=None, help="Repo root override")
    args = parser.parse_args()

    day = date.fromisoformat(args.date)
    selection = read_weekly_selection(args.root)
    if args.dry_run:
        path = daily_note_path(day, args.root)
        original = path.read_text(encoding="utf-8") if path.exists() else ""
        print(insert_or_replace_block(original, render_today_block(selection)))
        return 0
    print(update_daily_note(day, selection, args.root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
