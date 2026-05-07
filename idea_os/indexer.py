"""Markdown index generation for ideas, clusters, and research candidates."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from idea_os.models import total_maturity
from idea_os.store_paths import REPO_ROOT
from idea_os.yaml_io import load_yaml


def generate_indexes(ideas: list[dict[str, Any]], root: str | Path | None = None) -> tuple[Path, ...]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    index_dir = repo / "index"
    index_dir.mkdir(parents=True, exist_ok=True)
    idea_index = index_dir / "idea_index.md"
    tag_index = index_dir / "tag_index.md"
    cluster_index = index_dir / "cluster_index.md"
    research_index = index_dir / "research_candidate_index.md"
    idea_index.write_text(render_idea_index(ideas, repo), encoding="utf-8")
    tag_index.write_text(render_tag_index(ideas, repo), encoding="utf-8")
    cluster_index.write_text(render_cluster_index(_load_mapping(repo / "clusters" / "active_clusters.yaml")), encoding="utf-8")
    research_index.write_text(
        render_research_candidate_index(_load_mapping(repo / "research" / "research_candidates.yaml")),
        encoding="utf-8",
    )
    return idea_index, tag_index, cluster_index, research_index


def render_idea_index(ideas: list[dict[str, Any]], repo: Path) -> str:
    rows = [
        "# Idea Index",
        "",
        "| ID | Title | Maturity | Level | Status | Next Step | Path |",
        "| --- | --- | ---: | --- | --- | --- | --- |",
    ]
    for idea in sorted(ideas, key=lambda item: (-total_maturity(item), item["id"])):
        next_step = ""
        steps = idea.get("next_steps", [])
        if steps:
            next_step = str(steps[0])
        path = _relative_path(idea.get("_path", ""), repo)
        rows.append(
            f"| `{idea['id']}` | {idea.get('title', '')} | {idea.get('maturity_score', '0/100')} | `{idea.get('maturity_level', '')}` | `{idea.get('status', '')}` | {next_step} | `{path}` |"
        )
    rows.append("")
    rows.append("## Compact View")
    rows.append("")
    for idea in sorted(ideas, key=lambda item: item["id"]):
        rows.append(
            f"- {idea['id']} - {idea.get('title', '')} - {idea.get('maturity_score', '0/100')} - {idea.get('maturity_level', '')}"
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
            lines.append(
                f"- `{idea['id']}` - {idea.get('title', '')} (`{idea.get('maturity_level', '')}`, {idea.get('maturity_score', '0/100')}) - `{path}`"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_cluster_index(clusters: dict[str, Any]) -> str:
    lines = ["# Cluster Index", ""]
    if not clusters:
        lines.append("No active clusters generated.")
        return "\n".join(lines) + "\n"
    for cluster_id, cluster in sorted(clusters.items()):
        lines.append(
            f"- {cluster_id} - {cluster.get('theme', '')} - {cluster.get('cluster_score', '0/100')} - {cluster.get('recommendation', '')}"
        )
    return "\n".join(lines) + "\n"


def render_research_candidate_index(candidates: dict[str, Any]) -> str:
    lines = ["# Research Candidate Index", ""]
    if not candidates:
        lines.append("No research candidates generated.")
        return "\n".join(lines) + "\n"
    for candidate_id, candidate in sorted(candidates.items()):
        lines.append(
            f"- {candidate_id} - {candidate.get('title', '')} - {candidate.get('research_score', '0/100')} - {candidate.get('research_level', '')}"
        )
    return "\n".join(lines) + "\n"


def _load_mapping(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    loaded = load_yaml(path)
    return loaded if isinstance(loaded, dict) else {}


def _relative_path(path_text: str, repo: Path) -> str:
    if not path_text:
        return ""
    try:
        return str(Path(path_text).resolve().relative_to(repo))
    except ValueError:
        return path_text
