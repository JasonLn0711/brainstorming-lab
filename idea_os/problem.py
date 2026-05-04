"""Deterministic problem statement normalization."""

from __future__ import annotations

import re
from typing import Any


DEFAULT_CONSTRAINTS = ["limited resources", "evidence quality", "scope"]


def normalize_idea_problem(idea: dict[str, Any]) -> dict[str, Any]:
    existing = idea.get("problem_statement", {})
    raw = _raw_problem(existing) or str(idea.get("title", "")).strip()
    normalized_existing = _normalized_problem(existing)
    structure_existing = _structure(existing)

    if _is_complete_structure(structure_existing) and normalized_existing:
        status = "validated"
        normalized = normalized_existing
        structure = structure_existing
    else:
        structure, uncertain = infer_problem_structure(idea, raw)
        normalized = render_normalized_problem(structure)
        status = "needs_review" if uncertain else "normalized"

    idea["problem_statement"] = {
        "raw": raw,
        "normalized": normalized,
        "structure": structure,
    }
    idea["normalization_status"] = status
    return idea


def infer_problem_structure(idea: dict[str, Any], raw: str) -> tuple[dict[str, Any], bool]:
    text = " ".join(
        [
            raw,
            str(idea.get("title", "")),
            str(idea.get("summary", "")),
            " ".join(str(tag) for tag in idea.get("tags", [])),
            " ".join(str(item) for item in idea.get("assumptions", [])),
        ]
    )
    lower = text.lower()
    given = _extract_between(raw, "given", "optimize")
    optimize = _extract_between(raw, "optimize", "under")
    constraints = _extract_constraints(raw)

    if not given:
        given = _infer_given(lower, idea)
    if not optimize:
        optimize = _infer_optimize(lower, idea)
    if not constraints:
        constraints = _infer_constraints(lower, idea)

    uncertain = not raw or len(str(idea.get("summary", "")).strip()) < 30
    if not given or not optimize:
        uncertain = True
    return (
        {
            "given": given or "an unclear workflow or research opportunity",
            "optimize": optimize or "the next useful decision",
            "constraints": constraints or list(DEFAULT_CONSTRAINTS),
        },
        uncertain,
    )


def render_normalized_problem(structure: dict[str, Any]) -> str:
    given = str(structure.get("given", "")).strip().rstrip(".")
    optimize = str(structure.get("optimize", "")).strip().rstrip(".")
    constraints = structure.get("constraints", [])
    if isinstance(constraints, list):
        constraint_text = ", ".join(str(item).strip().rstrip(".") for item in constraints if str(item).strip())
    else:
        constraint_text = str(constraints).strip().rstrip(".")
    return f"Given {given}, optimize {optimize} under constraints of {constraint_text}."


def _raw_problem(problem: Any) -> str:
    if isinstance(problem, dict):
        return str(problem.get("raw", "")).strip() or str(problem.get("normalized", "")).strip()
    return str(problem or "").strip()


def _normalized_problem(problem: Any) -> str:
    if isinstance(problem, dict):
        return str(problem.get("normalized", "")).strip()
    return ""


def _structure(problem: Any) -> dict[str, Any]:
    if isinstance(problem, dict) and isinstance(problem.get("structure"), dict):
        structure = dict(problem["structure"])
        constraints = structure.get("constraints", [])
        if not isinstance(constraints, list):
            constraints = [str(constraints)]
        structure["constraints"] = constraints
        return structure
    return {"given": "", "optimize": "", "constraints": []}


def _is_complete_structure(structure: dict[str, Any]) -> bool:
    return bool(
        str(structure.get("given", "")).strip()
        and str(structure.get("optimize", "")).strip()
        and structure.get("constraints")
    )


def _extract_between(text: str, start: str, end: str) -> str:
    pattern = re.compile(rf"\b{start}\b(.*?)(?:\b{end}\b|$)", re.IGNORECASE)
    match = pattern.search(text)
    if not match:
        return ""
    value = match.group(1)
    value = re.sub(r"^[\s,:-]+", "", value)
    value = re.sub(r"[\s,.-]+$", "", value)
    return value.strip()


def _extract_constraints(text: str) -> list[str]:
    match = re.search(r"\bunder\b(?:\s+constraints?\s+of)?\s+(.*)", text, re.IGNORECASE)
    if not match:
        return []
    value = match.group(1).strip().rstrip(".")
    value = re.sub(r"^of\s+", "", value, flags=re.IGNORECASE)
    parts = re.split(r",|\band\b", value)
    return [part.strip() for part in parts if part.strip()]


def _infer_given(lower: str, idea: dict[str, Any]) -> str:
    if "patient" in lower or "clinical" in lower or "healthcare" in lower or "hospital" in lower:
        return "multiple patients entering a clinical workflow"
    if "cyber" in lower or "scam" in lower or "suspicious" in lower:
        return "high-volume suspicious content entering a review workflow"
    if "scheduler" in lower or "planning" in lower or "decision load" in lower:
        return "multiple commitments competing for limited planning capacity"
    if "workflow" in lower:
        return "a repeated workflow with observable bottlenecks"
    if "openclaw" in lower or "personal ops" in lower:
        return "Codex-heavy personal operations requiring safe automation"
    title = str(idea.get("title", "")).strip()
    return f"the idea '{title}'" if title else ""


def _infer_optimize(lower: str, idea: dict[str, Any]) -> str:
    if any(term in lower for term in ["triage", "priorit"]):
        return "prioritization and routing"
    if "review" in lower or "candidate" in lower:
        return "review-worthy candidate discovery"
    if "scheduler" in lower or "planning" in lower:
        return "sequencing of work and recovery"
    if "workflow" in lower:
        return "cycle time and decision quality"
    if "node" in lower or "automation" in lower or "openclaw" in lower:
        return "safe private operations support"
    return "the smallest useful next test"


def _infer_constraints(lower: str, idea: dict[str, Any]) -> list[str]:
    constraints: list[str] = []
    candidates = {
        "urgency": ["urgent", "urgency"],
        "fairness": ["fairness", "fair"],
        "safety": ["safety", "safe", "clinical"],
        "limited resources": ["limited", "capacity", "burden", "overloaded"],
        "auditability": ["audit", "provenance", "logging"],
        "privacy": ["privacy", "redaction", "patient"],
        "hard negatives": ["hard-negative", "hard negative"],
        "approval gates": ["approval", "rollback"],
    }
    for label, terms in candidates.items():
        if any(term in lower for term in terms):
            constraints.append(label)
    if not constraints:
        constraints.extend(str(tag) for tag in idea.get("tags", [])[:3])
    return constraints or list(DEFAULT_CONSTRAINTS)
