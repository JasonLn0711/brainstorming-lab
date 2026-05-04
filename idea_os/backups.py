"""Backup helpers for mutating canonical YAML records."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import shutil

from idea_os.store_paths import resolve_repo_root


def backup_file(path: str | Path, root: str | Path | None = None, run_id: str | None = None) -> Path | None:
    source = Path(path)
    if not source.exists():
        return None
    repo = resolve_repo_root(root)
    stamp = run_id or datetime.now().strftime("%Y%m%dT%H%M%S")
    try:
        relative = source.resolve().relative_to(repo)
    except ValueError:
        relative = Path(source.name)
    target = repo / "backups" / "idea_yaml" / stamp / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return target
