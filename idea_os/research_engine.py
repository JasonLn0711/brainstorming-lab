"""Generate research candidates from clusters."""

from __future__ import annotations

from typing import Any


def generate_research_candidates(
    clusters: dict[str, dict[str, Any]], ideas: list[dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    by_id = {idea["id"]: idea for idea in ideas}
    eligible: list[tuple[str, dict[str, Any]]] = []
    for cluster_id, cluster in clusters.items():
        cluster_ideas = [by_id[idea_id] for idea_id in cluster.get("ideas", []) if idea_id in by_id]
        if len(cluster_ideas) < 2:
            continue
        if float(cluster.get("avg_score", 0)) < 12:
            continue
        if not any(int(idea.get("maturity", {}).get("testability", 0)) >= 3 for idea in cluster_ideas):
            continue
        eligible.append((cluster_id, cluster))

    eligible.sort(key=lambda item: (-float(item[1].get("avg_score", 0)), item[0]))
    candidates: dict[str, dict[str, Any]] = {}
    for index, (cluster_id, cluster) in enumerate(eligible, start=1):
        candidates[f"research_candidate_{index:02d}"] = {
            "cluster_id": cluster_id,
            "theme": cluster.get("theme", ""),
            "ideas": cluster.get("ideas", []),
            "avg_score": cluster.get("avg_score", 0),
            "reason": [
                "cluster size >= 2",
                "average score >= 12",
                "at least one testable idea",
            ],
        }
    return candidates
