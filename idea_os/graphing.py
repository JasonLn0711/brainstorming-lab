"""Idea graph construction."""

from __future__ import annotations

from itertools import combinations
from typing import Any

from idea_os.similarity import idea_similarity, shared_tags


def build_graph(ideas: list[dict[str, Any]], threshold: float) -> dict[str, Any]:
    nodes = [
        {
            "id": idea["id"],
            "title": idea.get("title", ""),
            "status": idea.get("status", ""),
            "score": idea.get("score", 0),
            "tags": idea.get("tags", []),
            "path": idea.get("_path", ""),
        }
        for idea in sorted(ideas, key=lambda item: item["id"])
    ]
    edges: list[dict[str, Any]] = []
    for left, right in combinations(sorted(ideas, key=lambda item: item["id"]), 2):
        reasons: list[str] = []
        tags = shared_tags(left, right)
        similarity = idea_similarity(left, right)
        if right["id"] in left.get("connections", []) or left["id"] in right.get("connections", []):
            reasons.append("manual_connection")
        if tags:
            reasons.append("shared_tags")
        if similarity > threshold:
            reasons.append("semantic_similarity")
        if reasons:
            edges.append(
                {
                    "source": left["id"],
                    "target": right["id"],
                    "weight": round(max(similarity, 0.6 if tags else 0, 1.0 if "manual_connection" in reasons else 0), 4),
                    "similarity": similarity,
                    "shared_tags": tags,
                    "reasons": reasons,
                }
            )
    return {"nodes": nodes, "edges": edges}
