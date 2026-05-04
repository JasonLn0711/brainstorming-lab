"""Markdown index generation."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from idea_os.store import REPO_ROOT


def generate_indexes(ideas: list[dict[str, Any]], root: str | Path | None = None) -> tuple[Path, Path]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    index_dir = repo / "index"
    index_dir.mkdir(parents=True, exist_ok=True)
    idea_index = index_dir / "idea_index.md"
    tag_index = index_dir / "tag_index.md"
    idea_index.write_text(render_idea_index(ideas, repo), encoding="utf-8")
    tag_index.write_text(render_tag_index(ideas, repo), encoding="utf-8")
    return idea_index, tag_index


def render_idea_index(ideas: list[dict[str, Any]], repo: Path) -> str:
    rows = ["# Idea Index", "", "| ID | Title | Status | Score | Next Step | Path |", "| --- | --- | --- | ---: | --- | --- |"]
    for idea in sorted(ideas, key=lambda item: (-int(item.get("score", 0)), item["id"])):
        next_step = ""
        steps = idea.get("next_steps", [])
        if steps:
            next_step = str(steps[0])
        path = _relative_path(idea.get("_path", ""), repo)
        rows.append(
            f"| `{idea['id']}` | {idea.get('title', '')} | `{idea.get('status', '')}` | {idea.get('score', 0)} | {next_step} | `{path}` |"
        )
    return "\n".join(rows) + "\n"


def render_tag_index(ideas: list[dict[str, Any]], repo: Path) -> str:
    tags: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for idea in ideas:
        for tag in idea.get("tags", []):
            tags[str(tag)].append(idea)
    lines = ["# Tag Index", ""]
    for tag in sorted(tags):
        lines.append(f"## {tag}")
        lines.append("")
        for idea in sorted(tags[tag], key=lambda item: item["id"]):
            path = _relative_path(idea.get("_path", ""), repo)
            lines.append(f"- `{idea['id']}` - {idea.get('title', '')} (`{idea.get('status', '')}`, score {idea.get('score', 0)}) - `{path}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _relative_path(path_text: str, repo: Path) -> str:
    if not path_text:
        return ""
    try:
        return str(Path(path_text).resolve().relative_to(repo))
    except ValueError:
        return path_text
