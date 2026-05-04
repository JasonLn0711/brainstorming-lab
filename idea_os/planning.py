"""Planning repo integration helpers.

These helpers deliberately produce short bridge notes. The planning repo owns
capacity, priority, and links; this repo owns detailed thinking.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

from idea_os.config import planning_repo_path
from idea_os.store import REPO_ROOT
from idea_os.yaml_io import load_yaml, save_yaml


TODAY_START = "<!-- IDEA_OS_TODAY_START -->"
TODAY_END = "<!-- IDEA_OS_TODAY_END -->"
FEEDBACK_START = "<!-- IDEA_OS_FEEDBACK_START -->"
FEEDBACK_END = "<!-- IDEA_OS_FEEDBACK_END -->"


def iso_week_folder(day: date) -> str:
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


def daily_note_path(day: date, root: str | Path | None = None) -> Path:
    planning = planning_repo_path(root)
    return planning / "weeks" / iso_week_folder(day) / "days" / f"{day.isoformat()}.md"


def weekly_selection_path(root: str | Path | None = None) -> Path:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    return repo / "research" / "weekly_selection.yaml"


def read_weekly_selection(root: str | Path | None = None) -> dict[str, Any]:
    path = weekly_selection_path(root)
    if not path.exists():
        return {}
    data = load_yaml(path)
    return data if isinstance(data, dict) else {}


def render_weekly_bridge(selection: dict[str, Any]) -> str:
    lines = [
        "# Idea OS Weekly Selection",
        "",
        "This is a bridge file generated from `brainstorming-lab`.",
        "Keep detailed thinking in the idea YAML files.",
        "",
        "| Selection | Idea | Status | Score | Next test | Canonical path |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for key, item in selection.items():
        if not key.startswith("selection_") or not isinstance(item, dict):
            continue
        lines.append(
            "| {key} | `{id}` {title} | `{status}` | {score} | {next_step} | `{path}` |".format(
                key=key,
                id=item.get("id", ""),
                title=item.get("title", ""),
                status=item.get("status", ""),
                score=item.get("score", 0),
                next_step=item.get("next_step", ""),
                path=item.get("path", ""),
            )
        )
    return "\n".join(lines) + "\n"


def write_weekly_bridge(selection: dict[str, Any], root: str | Path | None = None) -> Path:
    generated_for = str(selection.get("week", iso_week_folder(date.today())))
    planning = planning_repo_path(root)
    target = planning / "weeks" / generated_for / "idea-os-weekly-selection.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_weekly_bridge(selection), encoding="utf-8")
    return target


def render_today_block(selection: dict[str, Any]) -> str:
    lines = [TODAY_START, "## Idea OS Suggestions", ""]
    entries = [
        item for key, item in selection.items() if key.startswith("selection_") and isinstance(item, dict)
    ]
    if not entries:
        lines.append("- No Idea OS suggestions selected.")
    for item in entries:
        lines.append(
            "- `{id}` {title} ({status}, score {score})".format(
                id=item.get("id", ""),
                title=item.get("title", ""),
                status=item.get("status", ""),
                score=item.get("score", 0),
            )
        )
        lines.append(f"  - Next test: {item.get('next_step', '')}")
        lines.append(f"  - Canonical path: `{item.get('path', '')}`")
        lines.append("  - Capacity impact: maybe")
    lines.append(TODAY_END)
    return "\n".join(lines) + "\n"


def insert_or_replace_block(original: str, block: str) -> str:
    if TODAY_START in original and TODAY_END in original:
        start = original.index(TODAY_START)
        end = original.index(TODAY_END) + len(TODAY_END)
        return original[:start] + block.rstrip() + original[end:]
    return original.rstrip() + "\n\n" + block


def update_daily_note(day: date, selection: dict[str, Any], root: str | Path | None = None) -> Path:
    path = daily_note_path(day, root)
    if path.exists():
        original = path.read_text(encoding="utf-8")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        original = f"# Daily note\n\n## Identity\n- Date: {day.isoformat()}\n- Week: {iso_week_folder(day)}\n"
    path.write_text(insert_or_replace_block(original, render_today_block(selection)), encoding="utf-8")
    return path


def extract_feedback_blocks(text: str) -> list[str]:
    blocks: list[str] = []
    cursor = 0
    while True:
        try:
            start = text.index(FEEDBACK_START, cursor) + len(FEEDBACK_START)
            end = text.index(FEEDBACK_END, start)
        except ValueError:
            break
        blocks.append(text[start:end].strip())
        cursor = end + len(FEEDBACK_END)
    return blocks


def load_feedback_from_daily(day: date, root: str | Path | None = None) -> dict[str, Any]:
    path = daily_note_path(day, root)
    if not path.exists():
        return {}
    feedback: dict[str, Any] = {}
    for block in extract_feedback_blocks(path.read_text(encoding="utf-8")):
        loaded = load_yaml_from_text(block)
        if isinstance(loaded, dict):
            feedback.update(loaded)
    return feedback


def load_yaml_from_text(text: str) -> Any:
    from idea_os.yaml_io import loads_yaml

    return loads_yaml(text)
