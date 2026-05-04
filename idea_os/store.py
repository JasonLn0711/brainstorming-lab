"""Filesystem store for Idea OS YAML records."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Any

from idea_os.models import score_idea
from idea_os.yaml_io import load_yaml, save_yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
IDEA_ID_PATTERN = re.compile(r"^idea_(\d{6})$")


STATUS_TO_DIR = {
    "raw": "raw",
    "emerging": "evolving",
    "structured": "structured",
    "research_ready": "structured",
    "executing": "executing",
    "archived": "archived",
}


def repo_root(root: str | Path | None = None) -> Path:
    return Path(root).resolve() if root is not None else REPO_ROOT


def idea_root(root: str | Path | None = None) -> Path:
    return repo_root(root) / "ideas"


def iter_idea_files(root: str | Path | None = None) -> list[Path]:
    base = idea_root(root)
    return sorted(path for path in base.glob("**/*.yaml") if path.is_file())


def load_idea(path: str | Path) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise ValueError(f"Idea file is not a mapping: {path}")
    data.setdefault("_path", str(Path(path).resolve()))
    return data


def load_all_ideas(root: str | Path | None = None) -> list[dict[str, Any]]:
    return [load_idea(path) for path in iter_idea_files(root)]


def save_idea(path: str | Path, idea: dict[str, Any]) -> Path:
    clean = {key: value for key, value in idea.items() if not key.startswith("_")}
    save_yaml(path, clean)
    return Path(path)


def find_idea_path(identifier: str, root: str | Path | None = None) -> Path:
    candidate = Path(identifier)
    if candidate.exists():
        return candidate
    for path in iter_idea_files(root):
        idea = load_idea(path)
        if idea.get("id") == identifier:
            return path
    raise FileNotFoundError(f"Could not find idea: {identifier}")


def next_idea_id(root: str | Path | None = None) -> str:
    highest = 0
    for path in iter_idea_files(root):
        idea = load_idea(path)
        match = IDEA_ID_PATTERN.match(str(idea.get("id", "")))
        if match:
            highest = max(highest, int(match.group(1)))
    return f"idea_{highest + 1:06d}"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return slug or "untitled_idea"


def idea_filename(idea: dict[str, Any]) -> str:
    return f"{idea['id']}_{slugify(str(idea.get('title', 'untitled')))[:64]}.yaml"


def path_for_idea(idea: dict[str, Any], root: str | Path | None = None) -> Path:
    status = str(idea.get("status", "raw"))
    folder = STATUS_TO_DIR.get(status, "raw")
    return idea_root(root) / folder / idea_filename(idea)


def save_and_move_idea(
    idea: dict[str, Any], old_path: str | Path | None = None, root: str | Path | None = None
) -> Path:
    target = path_for_idea(idea, root)
    if old_path is not None:
        old = Path(old_path)
        if old.exists() and old.parent.resolve() == target.parent.resolve():
            target = old
    save_idea(target, idea)
    if old_path is not None:
        old = Path(old_path)
        if old.exists() and old.resolve() != target.resolve():
            old.unlink()
    return target


def make_template_idea(
    idea_id: str,
    title: str,
    idea_type: str = "concept",
    tags: list[str] | None = None,
    created_at: str | None = None,
) -> dict[str, Any]:
    today = created_at or date.today().isoformat()
    idea = {
        "id": idea_id,
        "title": title,
        "created_at": today,
        "type": idea_type,
        "tags": tags or [],
        "status": "raw",
        "problem_statement": "Given an unclear opportunity, identify the useful problem and smallest test.",
        "summary": "A newly captured idea that needs structured development before it becomes work.",
        "assumptions": [],
        "insights": [],
        "connections": [],
        "value": {
            "impact": "medium",
            "feasibility": "medium",
        },
        "maturity": {
            "clarity": 1,
            "testability": 1,
            "connectedness": 0,
            "evidence": 0,
        },
        "score": 0,
        "next_steps": ["Write the smallest falsifiable test."],
        "source": ["conversation"],
    }
    return score_idea(idea)
