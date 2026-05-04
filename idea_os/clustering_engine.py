"""Cluster ideas from graph edges."""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Any

from idea_os.graphing import build_graph


def build_clusters(ideas: list[dict[str, Any]], threshold: float) -> dict[str, dict[str, Any]]:
    graph = build_graph(ideas, threshold)
    adjacency: dict[str, set[str]] = defaultdict(set)
    for edge in graph["edges"]:
        if "manual_connection" in edge["reasons"] or "semantic_similarity" in edge["reasons"]:
            adjacency[edge["source"]].add(edge["target"])
            adjacency[edge["target"]].add(edge["source"])

    by_id = {idea["id"]: idea for idea in ideas}
    seen: set[str] = set()
    components: list[list[str]] = []
    for idea_id in sorted(by_id):
        if idea_id in seen:
            continue
        queue = deque([idea_id])
        seen.add(idea_id)
        component: list[str] = []
        while queue:
            current = queue.popleft()
            component.append(current)
            for neighbor in sorted(adjacency[current]):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        components.append(sorted(component))

    components.sort(key=lambda ids: (-_avg_score(ids, by_id), ids[0]))
    clusters: dict[str, dict[str, Any]] = {}
    for index, ids in enumerate(components, start=1):
        key = f"cluster_{index:03d}"
        clusters[key] = {
            "theme": infer_theme([by_id[idea_id] for idea_id in ids]),
            "ideas": ids,
            "avg_score": round(_avg_score(ids, by_id), 2),
            "size": len(ids),
        }
    return clusters


def infer_theme(ideas: list[dict[str, Any]]) -> str:
    tag_counts: dict[str, int] = defaultdict(int)
    for idea in ideas:
        for tag in idea.get("tags", []):
            tag_counts[str(tag)] += 1
    if tag_counts:
        top_tags = sorted(tag_counts, key=lambda tag: (-tag_counts[tag], tag))[:3]
        return " / ".join(top_tags)
    return str(ideas[0].get("title", "untitled cluster")) if ideas else "empty cluster"


def _avg_score(ids: list[str], by_id: dict[str, dict[str, Any]]) -> float:
    if not ids:
        return 0.0
    return sum(int(by_id[idea_id].get("score", 0)) for idea_id in ids) / len(ids)
