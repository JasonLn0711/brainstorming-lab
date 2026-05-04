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


def selection_entries(selection: dict[str, Any], day: date | None = None) -> list[dict[str, Any]]:
    selected = selection.get("selected")
    if isinstance(selected, list):
        entries = [entry for entry in selected if isinstance(entry, dict)]
    else:
        entries = [
            item for key, item in selection.items() if key.startswith("selection_") and isinstance(item, dict)
        ]
    if day is None:
        return entries

    distribution = selection.get("daily_distribution", {})
    if not isinstance(distribution, dict):
        return entries
    idea_ids = distribution.get(day.isoformat(), [])
    if not isinstance(idea_ids, list):
        return []
    by_id = {entry.get("id"): entry for entry in entries}
    return [by_id[idea_id] for idea_id in idea_ids if idea_id in by_id]


def planning_canonical_path(path: str) -> str:
    if not path:
        return ""
    if path.startswith("/") or path.startswith("brainstorming-lab/"):
        return path
    return f"brainstorming-lab/{path}"


def render_weekly_bridge(selection: dict[str, Any]) -> str:
    lines = [
        "# Idea OS Weekly Selection",
        "",
        "This is a bridge file generated from `brainstorming-lab`.",
        "Keep detailed thinking in the idea YAML files.",
        "",
        f"- Week: {selection.get('week', '')}",
        f"- Adaptive epsilon: {selection.get('epsilon', '')}",
        f"- Reason: {selection.get('adaptive_reason', '')}",
        "",
        "## Selected Ideas",
        "",
        "| Idea | Type | Score | Novelty | Experiment | Measurable output | Canonical path |",
        "| --- | --- | ---: | ---: | --- | --- | --- |",
    ]
    for item in selection_entries(selection):
        lines.append(
            "| `{id}` {title} | `{selection_type}` | {score} | {novelty} | {experiment} | {measurable_output} | `{path}` |".format(
                id=item.get("id", ""),
                title=item.get("title", ""),
                selection_type=item.get("selection_type", ""),
                score=item.get("selection_score", item.get("score", 0)),
                novelty=item.get("novelty", ""),
                experiment=item.get("experiment", item.get("next_step", "")),
                measurable_output=item.get("measurable_output", ""),
                path=planning_canonical_path(str(item.get("path", ""))),
            )
        )
    lines.extend(["", "## Daily Distribution", ""])
    distribution = selection.get("daily_distribution", {})
    if isinstance(distribution, dict):
        by_id = {entry.get("id"): entry for entry in selection_entries(selection)}
        for day, idea_ids in distribution.items():
            labels = []
            if isinstance(idea_ids, list):
                for idea_id in idea_ids:
                    entry = by_id.get(idea_id, {})
                    labels.append(f"`{idea_id}` {entry.get('title', '')}".strip())
            lines.append(f"- {day}: {', '.join(labels) if labels else 'No Idea OS selection'}")
    return "\n".join(lines) + "\n"


def write_weekly_bridge(selection: dict[str, Any], root: str | Path | None = None) -> Path:
    generated_for = str(selection.get("week", iso_week_folder(date.today())))
    planning = planning_repo_path(root)
    target = planning / "weeks" / generated_for / "idea-os-weekly-selection.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_weekly_bridge(selection), encoding="utf-8")
    return target


def render_today_block(selection: dict[str, Any], day: date | None = None) -> str:
    lines = [TODAY_START, "## Idea OS Suggestions", ""]
    entries = selection_entries(selection, day)
    if not entries:
        lines.append("- No Idea OS suggestions selected.")
    for item in entries:
        lines.append(
            "- `{id}` {title} ({selection_type}, score {score}, novelty {novelty})".format(
                id=item.get("id", ""),
                title=item.get("title", ""),
                selection_type=item.get("selection_type", item.get("status", "")),
                score=item.get("selection_score", item.get("score", 0)),
                novelty=item.get("novelty", ""),
            )
        )
        lines.append(f"  - Experiment: {item.get('experiment', item.get('next_step', ''))}")
        lines.append(f"  - Measurable output: {item.get('measurable_output', '')}")
        lines.append(f"  - Canonical path: `{planning_canonical_path(str(item.get('path', '')))}`")
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
    path.write_text(insert_or_replace_block(original, render_today_block(selection, day)), encoding="utf-8")
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


def days_for_week(week: str) -> list[date]:
    year_text, week_text = week.split("-W", 1)
    year = int(year_text)
    week_number = int(week_text)
    return [date.fromisocalendar(year, week_number, weekday) for weekday in range(1, 6)]


def load_feedback_from_week(week: str, root: str | Path | None = None) -> dict[str, Any]:
    feedback: dict[str, Any] = {}
    for day in days_for_week(week):
        daily_feedback = load_feedback_from_daily(day, root)
        for idea_id, value in daily_feedback.items():
            if idea_id not in feedback:
                feedback[idea_id] = value
            elif isinstance(feedback[idea_id], dict) and isinstance(value, dict):
                feedback[idea_id].update(value)
    return feedback


def load_yaml_from_text(text: str) -> Any:
    from idea_os.yaml_io import loads_yaml

    return loads_yaml(text)
