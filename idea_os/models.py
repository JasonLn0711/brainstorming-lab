"""Idea data model, validation, and 100-point maturity scoring."""

from __future__ import annotations

import re
from typing import Any


REQUIRED_FIELDS = [
    "id",
    "title",
    "created_at",
    "status",
    "type",
    "tags",
    "problem_statement",
    "summary",
    "assumptions",
    "evidence",
    "baseline",
    "metrics",
    "maturity",
    "maturity_score",
    "maturity_level",
    "connections",
    "role",
    "next_steps",
]

IDEA_TYPES = {"concept", "question", "hypothesis", "project"}
STATUSES = {
    "raw",
    "emerging",
    "structured",
    "research_candidate",
    "execution_ready",
    "executing",
    "archived",
}
TERMINAL_STATUSES = {"executing", "archived"}

MATURITY_DIMENSIONS = {
    "problem_clarity": 15,
    "boundary_definition": 10,
    "testability": 15,
    "evidence_support": 15,
    "connection_strength": 10,
    "novelty": 10,
    "feasibility": 15,
    "research_potential": 10,
}

LEGACY_MATURITY_ALIASES = {
    "clarity": "problem_clarity",
    "connectedness": "connection_strength",
    "evidence": "evidence_support",
}


def format_score(value: int | float, denominator: int) -> str:
    return f"{int(round(float(value)))}/{denominator}"


def parse_score(value: Any, denominator: int = 100) -> int:
    if isinstance(value, (int, float)):
        return int(value)
    text = str(value or "").strip()
    if "/" in text:
        text = text.split("/", 1)[0]
    try:
        return int(float(text))
    except ValueError:
        return 0


def classify_maturity(score: int) -> str:
    score = max(0, min(100, int(score)))
    if score <= 20:
        return "raw"
    if score <= 40:
        return "emerging"
    if score <= 60:
        return "structured"
    if score <= 80:
        return "research_candidate"
    return "execution_ready"


def classify_score(score: int) -> str:
    """Compatibility alias for callers that previously asked for score levels."""

    return classify_maturity(score)


def maturity_action(level: str) -> str:
    return {
        "raw": "keep as raw idea",
        "emerging": "clarify and normalize problem statement",
        "structured": "include in graph and clustering",
        "research_candidate": "evaluate cluster readiness",
        "execution_ready": "generate experiment plan",
    }.get(level, "clarify next action")


def score_idea(
    idea: dict[str, Any],
    all_ideas: list[dict[str, Any]] | None = None,
    cluster_ids: list[str] | None = None,
    preserve_terminal: bool = True,
) -> dict[str, Any]:
    """Compute and store the strict 100-point maturity score.

    The old 20-point ``score`` field is removed so downstream code cannot
    accidentally keep using it as a decision input.
    """

    ensure_idea_defaults(idea)
    cluster_ids = cluster_ids or []
    maturity = idea.setdefault("maturity", {})
    subscores = {
        "problem_clarity": _score_problem_clarity(idea),
        "boundary_definition": _score_boundary_definition(idea),
        "testability": _score_testability(idea),
        "evidence_support": _score_evidence_support(idea),
        "connection_strength": _score_connection_strength(idea, all_ideas, cluster_ids),
        "novelty": _score_novelty(idea),
        "feasibility": _score_feasibility(idea),
        "research_potential": _score_research_potential(idea),
    }
    total = 0
    for field, denominator in MATURITY_DIMENSIONS.items():
        value = max(0, min(denominator, int(subscores[field])))
        maturity[field] = value
        maturity[f"{field}_score"] = format_score(value, denominator)
        total += value
    idea["maturity_score"] = format_score(total, 100)
    idea["maturity_level"] = classify_maturity(total)
    idea["maturity_action"] = maturity_action(idea["maturity_level"])
    idea.pop("score", None)

    current_status = str(idea.get("status", "raw"))
    if preserve_terminal and current_status in TERMINAL_STATUSES:
        idea["status"] = current_status
    else:
        idea["status"] = idea["maturity_level"]
    return idea


def validate_idea(idea: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in idea:
            errors.append(f"missing field: {field}")

    idea_type = idea.get("type")
    if idea_type is not None and idea_type not in IDEA_TYPES:
        errors.append(f"invalid type: {idea_type}")

    status = idea.get("status")
    if status is not None and status not in STATUSES:
        errors.append(f"invalid status: {status}")

    for list_field in ["tags", "assumptions", "evidence", "connections", "next_steps"]:
        if list_field in idea and not isinstance(idea[list_field], list):
            errors.append(f"{list_field} must be a list")

    problem = idea.get("problem_statement")
    if problem is not None and not isinstance(problem, dict):
        errors.append("problem_statement must be a mapping")
    elif isinstance(problem, dict):
        structure = problem.get("structure", {})
        if structure is not None and not isinstance(structure, dict):
            errors.append("problem_statement.structure must be a mapping")

    maturity = idea.get("maturity", {})
    if not isinstance(maturity, dict):
        errors.append("maturity must be a mapping")
    else:
        for field, denominator in MATURITY_DIMENSIONS.items():
            value = maturity.get(field, 0)
            if not isinstance(value, int) or value < 0 or value > denominator:
                errors.append(f"maturity.{field} must be an integer from 0 to {denominator}")

    total = parse_score(idea.get("maturity_score"), 100)
    if total < 0 or total > 100:
        errors.append("maturity_score must be from 0/100 to 100/100")

    level = idea.get("maturity_level")
    if level is not None and level not in {"raw", "emerging", "structured", "research_candidate", "execution_ready"}:
        errors.append(f"invalid maturity_level: {level}")
    return errors


def ensure_idea_defaults(idea: dict[str, Any]) -> dict[str, Any]:
    idea.setdefault("status", "raw")
    idea.setdefault("type", "concept")
    idea.setdefault("tags", [])
    idea.setdefault("summary", "")
    idea.setdefault("assumptions", [])
    idea.setdefault("connections", [])
    idea.setdefault("role", "idea")
    idea.setdefault("next_steps", [])
    idea.setdefault("baseline", [])
    idea.setdefault("metrics", [])
    idea.setdefault("evidence", _legacy_evidence(idea))
    idea.setdefault("insights", [])
    idea.setdefault("source", [])
    _ensure_problem_statement(idea)
    _ensure_maturity_shape(idea)
    return idea


def idea_search_text(idea: dict[str, Any]) -> str:
    parts: list[str] = []
    for field in ["title", "summary", "role"]:
        parts.append(str(idea.get(field, "")))
    problem = idea.get("problem_statement", {})
    if isinstance(problem, dict):
        parts.extend(str(problem.get(field, "")) for field in ["raw", "normalized"])
        structure = problem.get("structure", {})
        if isinstance(structure, dict):
            parts.extend(str(structure.get(field, "")) for field in ["given", "optimize"])
            constraints = structure.get("constraints", [])
            if isinstance(constraints, list):
                parts.extend(str(item) for item in constraints)
    else:
        parts.append(str(problem))
    for field in ["tags", "assumptions", "evidence", "baseline", "metrics", "insights", "next_steps", "source"]:
        values = idea.get(field, [])
        if isinstance(values, list):
            parts.extend(_text_from_value(value) for value in values)
        else:
            parts.append(str(values))
    return " ".join(parts)


def maturity_value(idea: dict[str, Any], field: str) -> int:
    return int(idea.get("maturity", {}).get(field, 0) or 0)


def total_maturity(idea: dict[str, Any]) -> int:
    return parse_score(idea.get("maturity_score"), 100)


def _ensure_problem_statement(idea: dict[str, Any]) -> None:
    problem = idea.get("problem_statement")
    if isinstance(problem, dict):
        structure = problem.setdefault("structure", {})
        if not isinstance(structure, dict):
            structure = {}
            problem["structure"] = structure
        problem.setdefault("raw", "")
        problem.setdefault("normalized", "")
        structure.setdefault("given", "")
        structure.setdefault("optimize", "")
        structure.setdefault("constraints", [])
        if not isinstance(structure["constraints"], list):
            structure["constraints"] = [str(structure["constraints"])]
        return
    raw = str(problem or "").strip()
    idea["problem_statement"] = {
        "raw": raw,
        "normalized": "",
        "structure": {
            "given": "",
            "optimize": "",
            "constraints": [],
        },
    }


def _ensure_maturity_shape(idea: dict[str, Any]) -> None:
    maturity = idea.setdefault("maturity", {})
    if not isinstance(maturity, dict):
        idea["maturity"] = {}
        maturity = idea["maturity"]
    legacy = dict(maturity)
    maturity.clear()
    for field, denominator in MATURITY_DIMENSIONS.items():
        legacy_value = legacy.get(field)
        if legacy_value is None:
            legacy_field = next((old for old, new in LEGACY_MATURITY_ALIASES.items() if new == field), None)
            if legacy_field:
                legacy_value = legacy.get(legacy_field)
        value = _scale_legacy_maturity(field, legacy_value, denominator)
        maturity[field] = value
        maturity[f"{field}_score"] = format_score(value, denominator)


def _legacy_evidence(idea: dict[str, Any]) -> list[Any]:
    evidence = idea.get("evidence")
    if isinstance(evidence, list):
        return evidence
    source = idea.get("source")
    if isinstance(source, list):
        return list(source)
    return []


def _scale_legacy_maturity(field: str, value: Any, denominator: int) -> int:
    if value is None:
        return 0
    try:
        numeric = int(value)
    except (TypeError, ValueError):
        return 0
    if numeric <= 5:
        if field in {"problem_clarity", "testability", "evidence_support"}:
            return round(numeric * denominator / 5)
        if field in {"connection_strength", "novelty", "research_potential"}:
            return round(numeric * denominator / 5)
        if field == "feasibility":
            return round(numeric * denominator / 5)
        if field == "boundary_definition":
            return round(numeric * denominator / 5)
    return max(0, min(denominator, numeric))


def _score_problem_clarity(idea: dict[str, Any]) -> int:
    problem = idea.get("problem_statement", {})
    if not isinstance(problem, dict):
        return 3 if str(problem).strip() else 0
    score = 0
    if str(problem.get("raw", "")).strip():
        score += 3
    if str(problem.get("normalized", "")).strip():
        score += 6
    structure = problem.get("structure", {})
    if isinstance(structure, dict):
        if (
            str(structure.get("given", "")).strip()
            and str(structure.get("optimize", "")).strip()
            and _list_has_items(structure.get("constraints", []))
        ):
            score += 6
    return min(score, 15)


def _score_boundary_definition(idea: dict[str, Any]) -> int:
    score = 0
    if _list_has_items(idea.get("tags", [])):
        score += 2
    text = idea_search_text(idea).lower()
    constraints = _problem_constraints(idea)
    if constraints or "scope" in text or "constraint" in text:
        score += 4
    if any(term in text for term in ["out of scope", "out-of-scope", "limitation", "not ", "not-", "boundary"]):
        score += 4
    return min(score, 10)


def _score_testability(idea: dict[str, Any]) -> int:
    score = 0
    if _list_has_items(idea.get("baseline", [])):
        score += 4
    if _list_has_items(idea.get("metrics", [])):
        score += 4
    text = idea_search_text(idea).lower()
    if any(term in text for term in ["input", "output", "fixture", "dataset", "synthetic", "benchmark"]):
        score += 3
    steps = " ".join(str(step).lower() for step in idea.get("next_steps", []) if step)
    if any(term in steps for term in ["test", "experiment", "prototype", "fixture", "measure", "evaluate", "define"]):
        score += 4
    return min(score, 15)


def _score_evidence_support(idea: dict[str, Any]) -> int:
    text = idea_search_text(idea).lower()
    score = 0
    if "observation" in text or "observed" in text:
        score += 3
    if any(term in text for term in ["case", "example", "fixture", "prior-project", "pilot"]):
        score += 3
    if any(term in text for term in ["dataset", "public data", "logs", "benchmark data"]):
        score += 3
    if any(term in text for term in ["literature", "benchmark", "paper", "reference"]):
        score += 3
    if any(term in text for term in ["real-world", "need", "workflow", "clinical", "review burden", "overloaded"]):
        score += 3
    return min(score, 15)


def _score_connection_strength(
    idea: dict[str, Any],
    all_ideas: list[dict[str, Any]] | None,
    cluster_ids: list[str],
) -> int:
    score = min(10, len(idea.get("connections", []) or []) * 2)
    if all_ideas:
        own_tags = {str(tag) for tag in idea.get("tags", [])}
        shared = 0
        for other in all_ideas:
            if other.get("id") == idea.get("id"):
                continue
            shared += len(own_tags & {str(tag) for tag in other.get("tags", [])})
        score += min(10 - score, shared)
    if cluster_ids:
        score += 3
    return min(score, 10)


def _score_novelty(idea: dict[str, Any]) -> int:
    text = idea_search_text(idea).lower()
    tags = {str(tag).lower() for tag in idea.get("tags", [])}
    if any(term in text for term in ["duplicate", "same method", "superseded"]):
        return 2
    if any(term in text for term in ["minor variation", "variant"]):
        return 5
    if any(term in text for term in ["research angle", "contribution", "novel", "original"]):
        return 10
    if idea.get("type") in {"hypothesis", "project"} and (tags or _problem_constraints(idea)):
        return 8
    if tags:
        return 6
    return 4


def _score_feasibility(idea: dict[str, Any]) -> int:
    text = idea_search_text(idea).lower()
    score = 0
    if any(term in text for term in ["synthetic", "without external data", "no real patient data", "local", "fixture"]):
        score += 5
    if any(term in text for term in ["tool", "model", "script", "python", "codex", "openclaw", "browser", "workflow"]):
        score += 4
    if any(term in text for term in ["one week", "bounded", "small", "tiny", "minimum viable", "first version"]):
        score += 3
    if any(term in text for term in ["low risk", "approval", "redaction", "rollback", "aggregate-only", "safety"]):
        score += 3
    return min(score, 15)


def _score_research_potential(idea: dict[str, Any]) -> int:
    text = idea_search_text(idea).lower()
    score = 0
    if any(term in text for term in ["research question", "question", "hypothesis"]):
        score += 3
    if _list_has_items(idea.get("metrics", [])) or "metric" in text:
        score += 2
    if any(term in text for term in ["contribution", "reduce", "improve", "compare", "novel"]):
        score += 3
    if idea.get("type") in {"project", "hypothesis"} or any(term in text for term in ["paper", "proposal", "prototype"]):
        score += 2
    return min(score, 10)


def _problem_constraints(idea: dict[str, Any]) -> list[Any]:
    problem = idea.get("problem_statement", {})
    if isinstance(problem, dict):
        structure = problem.get("structure", {})
        if isinstance(structure, dict):
            constraints = structure.get("constraints", [])
            if isinstance(constraints, list):
                return [item for item in constraints if str(item).strip()]
    return []


def _list_has_items(value: Any) -> bool:
    if not isinstance(value, list):
        return bool(value)
    return any(str(item).strip() for item in value)


def _text_from_value(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(str(part) for part in value.values())
    return str(value)
