"""Cluster ideas from merge-readiness relationships."""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Any

from idea_os.merge import score_merge_pair
from idea_os.models import maturity_value, total_maturity


def build_clusters(
    ideas: list[dict[str, Any]],
    threshold: float | int = 60,
) -> dict[str, dict[str, Any]]:
    minimum = int(float(threshold) * 100) if isinstance(threshold, float) and threshold <= 1 else int(threshold)
    by_id = {idea["id"]: idea for idea in ideas}
    adjacency: dict[str, set[str]] = defaultdict(set)
    edge_reasons: dict[tuple[str, str], dict[str, Any]] = {}

    ordered = sorted(ideas, key=lambda item: item["id"])
    for index, left in enumerate(ordered):
        for right in ordered[index + 1 :]:
            merge = score_merge_pair(left, right)
            if int(merge["merge_score_raw"]) >= minimum:
                adjacency[left["id"]].add(right["id"])
                adjacency[right["id"]].add(left["id"])
                edge_reasons[tuple(sorted([left["id"], right["id"]]))] = merge

    components = _components(sorted(by_id), adjacency)
    components = [component for component in components if len(component) >= 2]
    components.sort(key=lambda ids: (-_avg_maturity(ids, by_id), ids[0]))

    clusters: dict[str, dict[str, Any]] = {}
    for index, ids in enumerate(components, start=1):
        cluster_id = f"cluster_{index:04d}"
        cluster_ideas = [by_id[idea_id] for idea_id in ids]
        merge_edges = [
            edge_reasons[key]
            for left_index, left_id in enumerate(ids)
            for right_id in ids[left_index + 1 :]
            for key in [tuple(sorted([left_id, right_id]))]
            if key in edge_reasons
        ]
        average = round(_avg_maturity(ids, by_id))
        score = round(sum(int(edge["merge_score_raw"]) for edge in merge_edges) / len(merge_edges)) if merge_edges else average
        clusters[cluster_id] = {
            "theme": infer_theme(cluster_ideas),
            "cluster_type": "research_cluster",
            "ideas": ids,
            "normalized_problem": _representative_problem(cluster_ideas),
            "average_maturity_score": f"{average}/100",
            "cluster_score": f"{score}/100",
            "reason": _cluster_reasons(merge_edges),
            "recommendation": _cluster_recommendation(average, score),
            "averages": {
                "testability": f"{round(_avg_dimension(ids, by_id, 'testability'))}/15",
                "evidence_support": f"{round(_avg_dimension(ids, by_id, 'evidence_support'))}/15",
                "feasibility": f"{round(_avg_dimension(ids, by_id, 'feasibility'))}/15",
            },
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


def _components(ids: list[str], adjacency: dict[str, set[str]]) -> list[list[str]]:
    seen: set[str] = set()
    components: list[list[str]] = []
    for idea_id in ids:
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
    return components


def _avg_maturity(ids: list[str], by_id: dict[str, dict[str, Any]]) -> float:
    if not ids:
        return 0.0
    return sum(total_maturity(by_id[idea_id]) for idea_id in ids) / len(ids)


def _avg_dimension(ids: list[str], by_id: dict[str, dict[str, Any]], dimension: str) -> float:
    if not ids:
        return 0.0
    return sum(maturity_value(by_id[idea_id], dimension) for idea_id in ids) / len(ids)


def _representative_problem(ideas: list[dict[str, Any]]) -> str:
    for idea in sorted(ideas, key=lambda item: -total_maturity(item)):
        problem = idea.get("problem_statement", {})
        if isinstance(problem, dict) and problem.get("normalized"):
            return str(problem["normalized"])
    return ""


def _cluster_reasons(edges: list[dict[str, Any]]) -> list[str]:
    reasons: list[str] = []
    for edge in edges:
        for reason in edge.get("reason", []):
            if reason not in reasons:
                reasons.append(reason)
    return reasons[:8] or ["merge score threshold met"]


def _cluster_recommendation(average_maturity: int, cluster_score: int) -> str:
    if average_maturity >= 80 and cluster_score >= 75:
        return "prepare experiment plan"
    if average_maturity >= 65 and cluster_score >= 60:
        return "evaluate as research candidate"
    return "keep clustered and improve maturity"
