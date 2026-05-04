"""Merge-readiness scoring for related idea pairs."""

from __future__ import annotations

from itertools import combinations
from typing import Any

from idea_os.models import idea_search_text
from idea_os.similarity import idea_similarity, shared_tags, tokenize


MERGE_DIMENSIONS = {
    "normalized_problem_similarity": 25,
    "semantic_similarity": 15,
    "tag_overlap": 10,
    "complementary_value": 20,
    "evidence_alignment": 10,
    "complexity_control": 20,
}


def format_score(value: int, denominator: int = 100) -> str:
    return f"{int(value)}/{denominator}"


def merge_decision(score: int) -> str:
    if score <= 39:
        return "do_not_merge"
    if score <= 59:
        return "keep_related"
    if score <= 74:
        return "suggest_cluster"
    if score <= 89:
        return "strong_cluster_or_synthesis"
    return "duplicate_merge"


def recommended_action(decision: str, merge_type: str) -> str:
    if decision == "do_not_merge":
        return "do_not_merge"
    if decision == "keep_related":
        return "keep_related"
    if merge_type == "duplicate_merge":
        return "duplicate_merge"
    if merge_type == "research_synthesis":
        return "research_synthesis"
    return "create_cluster"


def score_merge_pair(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    normalized_similarity = _normalized_problem_similarity(left, right)
    semantic = idea_similarity(left, right)
    tags = shared_tags(left, right)
    complementary = _complementary_value(left, right)
    evidence = _evidence_alignment(left, right)
    complexity = _complexity_control(left, right)
    subscores = {
        "normalized_problem_similarity": round(normalized_similarity * 25),
        "semantic_similarity": round(semantic * 15),
        "tag_overlap": min(10, len(tags) * 4),
        "complementary_value": complementary,
        "evidence_alignment": evidence,
        "complexity_control": complexity,
    }
    total = sum(subscores.values())
    merge_type = _merge_type(left, right, total, normalized_similarity, semantic, complementary)
    decision = merge_decision(total)
    return {
        "ideas": [left["id"], right["id"]],
        "merge_type": merge_type,
        "merge_score": format_score(total),
        "merge_score_raw": total,
        "decision": decision,
        "confidence": _confidence(total),
        "subscores": {key: format_score(value, MERGE_DIMENSIONS[key]) for key, value in subscores.items()},
        "shared_tags": tags,
        "reason": _reasons(left, right, subscores, tags),
        "recommended_action": recommended_action(decision, merge_type),
    }


def detect_merge_candidates(ideas: list[dict[str, Any]], minimum_score: int = 40) -> dict[str, dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for left, right in combinations(sorted(ideas, key=lambda item: item["id"]), 2):
        candidate = score_merge_pair(left, right)
        if int(candidate["merge_score_raw"]) >= minimum_score:
            candidates.append(candidate)
    candidates.sort(key=lambda item: (-int(item["merge_score_raw"]), item["ideas"]))
    return {
        f"merge_candidate_{index:04d}": _public_candidate(candidate, index)
        for index, candidate in enumerate(candidates, start=1)
    }


def _public_candidate(candidate: dict[str, Any], index: int) -> dict[str, Any]:
    return {
        "candidate_id": f"merge_candidate_{index:04d}",
        "ideas": candidate["ideas"],
        "merge_type": candidate["merge_type"],
        "merge_score": candidate["merge_score"],
        "confidence": candidate["confidence"],
        "reason": candidate["reason"],
        "recommended_action": candidate["recommended_action"],
        "decision": candidate["decision"],
        "subscores": candidate["subscores"],
        "shared_tags": candidate["shared_tags"],
    }


def _normalized_problem_similarity(left: dict[str, Any], right: dict[str, Any]) -> float:
    left_text = _normalized_text(left)
    right_text = _normalized_text(right)
    if not left_text or not right_text:
        return 0.0
    left_tokens = set(tokenize(left_text))
    right_tokens = set(tokenize(right_text))
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens | right_tokens)


def _normalized_text(idea: dict[str, Any]) -> str:
    problem = idea.get("problem_statement", {})
    if isinstance(problem, dict):
        return str(problem.get("normalized", "") or problem.get("raw", ""))
    return str(problem or "")


def _complementary_value(left: dict[str, Any], right: dict[str, Any]) -> int:
    if right["id"] in left.get("connections", []) or left["id"] in right.get("connections", []):
        return 18
    left_role = str(left.get("role", "")).lower()
    right_role = str(right.get("role", "")).lower()
    if left_role and right_role and left_role != right_role:
        return 16
    left_text = idea_search_text(left).lower()
    right_text = idea_search_text(right).lower()
    method_terms = ["baseline", "metric", "workflow", "model", "interface", "evaluation", "evidence"]
    shared_methods = sum(1 for term in method_terms if term in left_text and term in right_text)
    if shared_methods >= 3:
        return 12
    return 8


def _evidence_alignment(left: dict[str, Any], right: dict[str, Any]) -> int:
    left_text = " ".join(str(item).lower() for item in left.get("evidence", []))
    right_text = " ".join(str(item).lower() for item in right.get("evidence", []))
    if not left_text or not right_text:
        return 2
    shared = set(tokenize(left_text)) & set(tokenize(right_text))
    if shared:
        return min(10, 4 + len(shared))
    if any(term in left_text + right_text for term in ["observation", "prior-project", "benchmark", "dataset"]):
        return 5
    return 3


def _complexity_control(left: dict[str, Any], right: dict[str, Any]) -> int:
    combined_tags = set(str(tag) for tag in left.get("tags", [])) | set(str(tag) for tag in right.get("tags", []))
    combined_steps = len(left.get("next_steps", []) or []) + len(right.get("next_steps", []) or [])
    score = 20
    if len(combined_tags) > 8:
        score -= 5
    if combined_steps > 6:
        score -= 5
    if not shared_tags(left, right):
        score -= 4
    return max(4, score)


def _merge_type(
    left: dict[str, Any],
    right: dict[str, Any],
    total: int,
    normalized_similarity: float,
    semantic: float,
    complementary: int,
) -> str:
    if total >= 90 and normalized_similarity >= 0.75 and semantic >= 0.75 and complementary <= 12:
        return "duplicate_merge"
    if total >= 75 and complementary >= 16:
        return "research_synthesis"
    return "cluster_merge"


def _confidence(score: int) -> str:
    if score >= 80:
        return "high"
    if score >= 60:
        return "medium"
    return "low"


def _reasons(left: dict[str, Any], right: dict[str, Any], subscores: dict[str, int], tags: list[str]) -> list[str]:
    reasons: list[str] = []
    if subscores["normalized_problem_similarity"] >= 12:
        reasons.append("normalized problem statements are similar")
    if subscores["semantic_similarity"] >= 8:
        reasons.append("idea text has semantic overlap")
    if tags:
        reasons.append("shared tags: " + ", ".join(tags))
    if right["id"] in left.get("connections", []) or left["id"] in right.get("connections", []):
        reasons.append("manual connection exists")
    if subscores["complementary_value"] >= 16:
        reasons.append("roles or methods are complementary")
    if not reasons:
        reasons.append("weak relation retained for review")
    return reasons
