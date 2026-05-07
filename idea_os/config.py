"""Configuration loading."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from idea_os.store import REPO_ROOT
from idea_os.yaml_io import load_yaml


DEFAULT_CONFIG = {
    "planning_repo_path": "../planning-everything-track",
    "top_n": 5,
    "similarity_threshold": 0.75,
    "priority_tags": ["cybersecurity", "workflow", "planning-bridge", "evidence-routing"],
    "base_epsilon": 0.3,
    "min_epsilon": 0.1,
    "max_epsilon": 0.4,
    "selection_seed": "iso_week",
}


def load_config(root: str | Path | None = None) -> dict[str, Any]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    path = repo / "config" / "settings.yaml"
    config = dict(DEFAULT_CONFIG)
    if path.exists():
        loaded = load_yaml(path)
        if isinstance(loaded, dict):
            config.update(loaded)
    return config


def planning_repo_path(root: str | Path | None = None) -> Path:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    configured = str(load_config(repo).get("planning_repo_path", DEFAULT_CONFIG["planning_repo_path"]))
    return (repo / configured).resolve()
