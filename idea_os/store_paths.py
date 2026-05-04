"""Shared path helpers that do not import the store layer."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def resolve_repo_root(root: str | Path | None = None) -> Path:
    return Path(root).resolve() if root is not None else REPO_ROOT
