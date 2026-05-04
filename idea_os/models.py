"""Idea data model, validation, and scoring."""

from __future__ import annotations

from typing import Any


REQUIRED_FIELDS = [
    "id",
    "title",
    "created_at",
    "type",
    "tags",
    "status",
    "problem_statement",
    "summary",
    "assumptions",
    "insights",
    "connections",
    "value",
    "maturity",
    "score",
    "next_steps",
    "source",
]

IDEA_TYPES = {"concept", "question", "hypothesis", "project"}
STATUSES = {"raw", "emerging", "structured", "research_ready", "executing", "archived"}
MATURITY_FIELDS = ["clarity", "testability", "connectedness", "evidence"]
TERMINAL_STATUSES = {"executing", "archived"}


def classify_score(score: int) -> str:
    if score <= 5:
        return "raw"
    if score <= 10:
        return "emerging"
    if score <= 15:
        return "structured"
    return "research_ready"


def score_idea(idea: dict[str, Any], preserve_terminal: bool = True) -> dict[str, Any]:
    maturity = idea.setdefault("maturity", {})
    total = 0
    for field in MATURITY_FIELDS:
        value = _as_int(maturity.get(field, 0))
        value = max(0, min(5, value))
        maturity[field] = value
        total += value
    idea["score"] = total
    current_status = str(idea.get("status", "raw"))
    if preserve_terminal and current_status in TERMINAL_STATUSES:
        idea["status"] = current_status
    else:
        idea["status"] = classify_score(total)
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

    for list_field in ["tags", "assumptions", "insights", "connections", "next_steps", "source"]:
        if list_field in idea and not isinstance(idea[list_field], list):
            errors.append(f"{list_field} must be a list")

    maturity = idea.get("maturity", {})
    if not isinstance(maturity, dict):
        errors.append("maturity must be a mapping")
    else:
        for field in MATURITY_FIELDS:
            value = maturity.get(field, 0)
            if not isinstance(value, int) or value < 0 or value > 5:
                errors.append(f"maturity.{field} must be an integer from 0 to 5")

    score = idea.get("score", 0)
    if not isinstance(score, int) or score < 0 or score > 20:
        errors.append("score must be an integer from 0 to 20")
    return errors


def idea_search_text(idea: dict[str, Any]) -> str:
    parts: list[str] = []
    for field in ["title", "problem_statement", "summary"]:
        parts.append(str(idea.get(field, "")))
    for field in ["tags", "assumptions", "insights", "next_steps", "source"]:
        values = idea.get(field, [])
        if isinstance(values, list):
            parts.extend(str(value) for value in values)
    return " ".join(parts)


def _as_int(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0
