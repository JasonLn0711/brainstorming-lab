"""Scientific paper quality evaluation validation.

This module validates the post-reading paper-quality score. It is intentionally
separate from paper triage: triage decides which paper to read, while this file
checks whether the selected paper's scientific claims are well supported.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from idea_os.store import REPO_ROOT
from idea_os.yaml_io import load_yaml


RUBRIC_VERSION = "scientific_paper_evaluation_v1"

VALID_STATUSES = {"not_started", "preliminary", "final", "parked"}
VALID_COEFFICIENTS = {0, 0.25, 0.5, 0.75, 1}
VALID_RISK_LEVELS = {"not_evaluated", "low", "medium", "high", "critical"}
VALID_DECISIONS = {
    "not_evaluated",
    "strong_reject",
    "reject",
    "weak_reject",
    "borderline",
    "weak_accept",
    "accept",
    "strong_accept",
}

DIMENSIONS: dict[str, dict[str, Any]] = {
    "problem_value": {
        "max": 12,
        "items": {
            "A1_problem_clarity": 3,
            "A2_importance": 3,
            "A3_researchability": 2,
            "A4_practical_or_theoretical_impact": 2,
            "A5_timeliness": 2,
        },
    },
    "literature_gap": {
        "max": 10,
        "items": {
            "B1_core_literature_coverage": 3,
            "B2_prior_work_accuracy": 2,
            "B3_clear_research_gap": 3,
            "B4_avoids_strawman": 2,
        },
    },
    "contribution_novelty": {
        "max": 12,
        "items": {
            "C1_explicit_contributions": 2,
            "C2_novelty": 4,
            "C3_beyond_engineering_integration": 2,
            "C4_alignment_with_problem": 2,
            "C5_extensibility": 2,
        },
    },
    "method_soundness": {
        "max": 16,
        "items": {
            "D1_method_clarity": 3,
            "D2_assumption_clarity": 3,
            "D3_method_problem_fit": 3,
            "D4_technical_correctness": 3,
            "D5_complete_system_or_process": 2,
            "D6_cost_and_complexity_awareness": 2,
        },
    },
    "evidence_experiment": {
        "max": 20,
        "items": {
            "E1_evaluation_matches_claims": 4,
            "E2_fair_baselines": 3,
            "E3_dataset_or_sample_quality": 3,
            "E4_ablation_or_component_analysis": 3,
            "E5_statistical_validity": 3,
            "E6_failure_case_analysis": 2,
            "E7_leakage_or_contamination_prevention": 2,
        },
    },
    "results_analysis": {
        "max": 10,
        "items": {
            "F1_clear_result_presentation": 2,
            "F2_analysis_depth": 3,
            "F3_results_support_claims": 3,
            "F4_tradeoff_discussion": 2,
        },
    },
    "reproducibility": {
        "max": 10,
        "items": {
            "G1_code_availability": 2,
            "G2_data_availability_or_protocol": 2,
            "G3_experimental_settings": 2,
            "G4_environment_and_dependencies": 2,
            "G5_reproduction_steps": 2,
        },
    },
    "scientific_honesty": {
        "max": 6,
        "items": {
            "H1_limitation_disclosure": 2,
            "H2_claim_restraint": 2,
            "H3_ethics_bias_risk_disclosure": 2,
        },
    },
    "communication": {
        "max": 4,
        "items": {
            "I1_structure": 1,
            "I2_figures_and_tables": 1,
            "I3_writing_precision": 1,
            "I4_abstract_conclusion_accuracy": 1,
        },
    },
}

PENALTIES: dict[str, int] = {
    "mild_overclaim": 3,
    "moderate_overclaim": 6,
    "severe_overclaim": 10,
    "missing_important_baseline": 5,
    "missing_variance_ci_or_repeats": 3,
    "misleading_figures": 3,
    "cherry_picking": 5,
    "thin_limitations": 3,
    "missing_failure_case_discussion": 3,
    "unclear_data_source": 5,
    "unclear_annotation_process": 3,
    "unvalidated_llm_judge": 4,
    "missing_prompt_or_model_version": 3,
    "cybersecurity_missing_misuse_boundary": 4,
    "biomedical_missing_ethics_or_clinical_limits": 5,
}

CAPS: dict[str, int] = {
    "core_method_major_error": 55,
    "clear_data_leakage": 50,
    "experiments_do_not_support_main_claim": 60,
    "clearly_unfair_baseline": 70,
    "no_evidence_for_core_claim": 50,
    "severe_overclaim": 65,
    "severe_ethics_or_privacy_issue": 60,
    "suspected_fabrication_or_unexplained_anomaly": 40,
    "method_too_unclear_to_understand": 65,
    "not_reproducible_without_reason": 75,
    "missing_core_literature_invalidates_novelty": 70,
}

CONFIDENCE_ITEMS: dict[str, int] = {
    "full_text_available": 10,
    "supplementary_material_available": 10,
    "code_data_or_appendix_checkable": 15,
    "evaluator_domain_background": 15,
    "all_subscores_have_evidence_notes": 20,
    "two_independent_reviewers": 15,
    "disagreement_adjudicated": 15,
}

OVERCLAIM_CHECKS = [
    "overly_strong_conclusion_language",
    "small_sample_to_broad_claim",
    "offline_benchmark_to_real_world_deployment",
    "correlation_as_causation",
    "prototype_as_production_ready",
    "synthetic_result_as_real_world_validation",
    "ignores_failure_cases",
    "hides_negative_results",
]


def quality_evaluation_files(root: str | Path | None = None) -> list[Path]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    papers_dir = repo / "weekly-paper-lab" / "papers"
    if not papers_dir.exists():
        return []
    return sorted(paper_dir / "scientific_evaluation.yaml" for paper_dir in papers_dir.iterdir() if paper_dir.is_dir())


def validate_quality_evaluation_file(
    path: str | Path,
    root: str | Path | None = None,
    expected_paper_id: str | None = None,
) -> list[str]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    eval_path = Path(path).resolve()
    label = _rel(eval_path, repo)
    if not eval_path.exists():
        return [f"{label}: missing scientific_evaluation.yaml"]
    try:
        data = load_yaml(eval_path)
    except Exception as exc:
        return [f"{label}: could not parse YAML: {exc}"]
    if not isinstance(data, dict):
        return [f"{label}: scientific_evaluation.yaml must be a mapping"]
    errors = validate_quality_evaluation(data, label)
    if expected_paper_id is not None and data.get("paper_id") != expected_paper_id:
        errors.append(f"{label}: paper_id must match paper.yaml paper_id {expected_paper_id}")
    return errors


def validate_quality_evaluation(data: dict[str, Any], label: str = "scientific_evaluation.yaml") -> list[str]:
    errors: list[str] = []

    if data.get("rubric_version") != RUBRIC_VERSION:
        errors.append(f"{label}: rubric_version must be {RUBRIC_VERSION}")
    status = data.get("evaluation_status")
    if status not in VALID_STATUSES:
        errors.append(f"{label}: evaluation_status must be one of {sorted(VALID_STATUSES)}")
    if not str(data.get("paper_id", "")).strip():
        errors.append(f"{label}: paper_id is required")
    if not str(data.get("paper_type", "")).strip():
        errors.append(f"{label}: paper_type is required")

    dimension_errors, raw_score = _validate_dimensions(data.get("dimensions"), label)
    errors.extend(dimension_errors)

    penalty_errors, penalty_total = _validate_penalties(data.get("penalties"), label)
    errors.extend(penalty_errors)

    cap_errors, applied_cap = _validate_caps(data.get("caps"), label)
    errors.extend(cap_errors)

    quality = data.get("quality_score")
    if not isinstance(quality, dict):
        errors.append(f"{label}: quality_score must be a mapping")
    else:
        if not _same_number(quality.get("raw_score"), raw_score):
            errors.append(f"{label}: quality_score.raw_score must be {_fmt(raw_score)}")
        if not _same_number(quality.get("penalty_total"), penalty_total):
            errors.append(f"{label}: quality_score.penalty_total must be {_fmt(penalty_total)}")
        expected_cap = applied_cap if applied_cap is not None else None
        if quality.get("applied_cap") != expected_cap:
            errors.append(f"{label}: quality_score.applied_cap must be {expected_cap}")
        expected_final = max(0.0, raw_score - penalty_total)
        if applied_cap is not None:
            expected_final = min(expected_final, float(applied_cap))
        if not _same_number(quality.get("final_score"), expected_final):
            errors.append(f"{label}: quality_score.final_score must be {_fmt(expected_final)}")
        decision = quality.get("decision")
        if decision not in VALID_DECISIONS:
            errors.append(f"{label}: quality_score.decision must be one of {sorted(VALID_DECISIONS)}")
        if status != "not_started" and decision == "not_evaluated":
            errors.append(f"{label}: quality_score.decision cannot be not_evaluated after scoring starts")

    confidence_errors, confidence_score = _validate_confidence(data.get("confidence_score"), label)
    errors.extend(confidence_errors)
    confidence = data.get("confidence_score")
    if isinstance(confidence, dict) and not _same_number(confidence.get("score"), confidence_score):
        errors.append(f"{label}: confidence_score.score must be {_fmt(confidence_score)}")

    errors.extend(_validate_overclaim_risk(data.get("overclaim_risk"), status, label))
    errors.extend(_validate_reproducibility_risk(data.get("reproducibility_risk"), status, label))
    errors.extend(_validate_reviewer_consistency(data.get("reviewer_consistency"), label))
    return errors


def blank_quality_evaluation(paper_id: str, paper_type: str = "system_paper") -> dict[str, Any]:
    dimensions: dict[str, Any] = {}
    for dimension, rule in DIMENSIONS.items():
        items = {}
        for item, weight in rule["items"].items():
            items[item] = {
                "weight": weight,
                "coefficient": 0,
                "score": 0,
                "evidence_note": "Not evaluated yet.",
            }
        dimensions[dimension] = {"score": 0, "max": rule["max"], "items": items}

    return {
        "paper_id": paper_id,
        "rubric_version": RUBRIC_VERSION,
        "evaluation_status": "not_started",
        "evaluated_at": "",
        "evaluator": "",
        "paper_type": paper_type,
        "field": "",
        "quality_score": {
            "raw_score": 0,
            "penalty_total": 0,
            "applied_cap": None,
            "final_score": 0,
            "decision": "not_evaluated",
        },
        "dimensions": dimensions,
        "penalties": {
            key: {"applied": False, "deduction": 0, "evidence_note": "Not evaluated yet."}
            for key in PENALTIES
        },
        "caps": {
            key: {"applied": False, "cap": cap, "evidence_note": "Not evaluated yet."}
            for key, cap in CAPS.items()
        },
        "confidence_score": {
            "score": 0,
            "items": {
                key: {"present": False, "points": points, "evidence_note": "Not evaluated yet."}
                for key, points in CONFIDENCE_ITEMS.items()
            },
        },
        "overclaim_risk": {
            "level": "not_evaluated",
            "checklist": {
                key: {"yes": False, "evidence_note": "Not evaluated yet."}
                for key in OVERCLAIM_CHECKS
            },
        },
        "reproducibility_risk": {
            "level": "not_evaluated",
            "evidence_note": "Not evaluated yet.",
        },
        "reviewer_consistency": {
            "reviewer_count": 0,
            "score_gap": None,
            "requires_adjudication": False,
            "disagreement_note": "",
        },
    }


def _validate_dimensions(value: Any, label: str) -> tuple[list[str], float]:
    if not isinstance(value, dict):
        return [f"{label}: dimensions must be a mapping"], 0.0
    errors: list[str] = []
    raw_score = 0.0
    for dimension, rule in DIMENSIONS.items():
        dimension_label = f"{label}: dimensions.{dimension}"
        dimension_value = value.get(dimension)
        if not isinstance(dimension_value, dict):
            errors.append(f"{dimension_label} must be a mapping")
            continue
        if dimension_value.get("max") != rule["max"]:
            errors.append(f"{dimension_label}.max must be {rule['max']}")
        items = dimension_value.get("items")
        if not isinstance(items, dict):
            errors.append(f"{dimension_label}.items must be a mapping")
            continue
        dimension_score = 0.0
        for item, weight in rule["items"].items():
            item_label = f"{dimension_label}.items.{item}"
            item_value = items.get(item)
            if not isinstance(item_value, dict):
                errors.append(f"{item_label} must be a mapping")
                continue
            if item_value.get("weight") != weight:
                errors.append(f"{item_label}.weight must be {weight}")
            coefficient = item_value.get("coefficient")
            if not _valid_coefficient(coefficient):
                errors.append(f"{item_label}.coefficient must be one of {sorted(VALID_COEFFICIENTS)}")
                continue
            expected_score = weight * float(coefficient)
            if not _same_number(item_value.get("score"), expected_score):
                errors.append(f"{item_label}.score must be {_fmt(expected_score)}")
            if not str(item_value.get("evidence_note", "")).strip():
                errors.append(f"{item_label}.evidence_note is required")
            dimension_score += expected_score
        if not _same_number(dimension_value.get("score"), dimension_score):
            errors.append(f"{dimension_label}.score must be {_fmt(dimension_score)}")
        raw_score += dimension_score
    return errors, raw_score


def _validate_penalties(value: Any, label: str) -> tuple[list[str], float]:
    if not isinstance(value, dict):
        return [f"{label}: penalties must be a mapping"], 0.0
    errors: list[str] = []
    total = 0.0
    for key, deduction in PENALTIES.items():
        entry_label = f"{label}: penalties.{key}"
        entry = value.get(key)
        if not isinstance(entry, dict):
            errors.append(f"{entry_label} must be a mapping")
            continue
        applied = entry.get("applied")
        if not isinstance(applied, bool):
            errors.append(f"{entry_label}.applied must be true or false")
            continue
        expected = deduction if applied else 0
        if not _same_number(entry.get("deduction"), expected):
            errors.append(f"{entry_label}.deduction must be {expected}")
        if applied and not str(entry.get("evidence_note", "")).strip():
            errors.append(f"{entry_label}.evidence_note is required when applied")
        total += expected
    return errors, total


def _validate_caps(value: Any, label: str) -> tuple[list[str], int | None]:
    if not isinstance(value, dict):
        return [f"{label}: caps must be a mapping"], None
    errors: list[str] = []
    active_caps: list[int] = []
    for key, cap in CAPS.items():
        entry_label = f"{label}: caps.{key}"
        entry = value.get(key)
        if not isinstance(entry, dict):
            errors.append(f"{entry_label} must be a mapping")
            continue
        applied = entry.get("applied")
        if not isinstance(applied, bool):
            errors.append(f"{entry_label}.applied must be true or false")
            continue
        if entry.get("cap") != cap:
            errors.append(f"{entry_label}.cap must be {cap}")
        if applied:
            active_caps.append(cap)
            if not str(entry.get("evidence_note", "")).strip():
                errors.append(f"{entry_label}.evidence_note is required when applied")
    return errors, min(active_caps) if active_caps else None


def _validate_confidence(value: Any, label: str) -> tuple[list[str], float]:
    if not isinstance(value, dict):
        return [f"{label}: confidence_score must be a mapping"], 0.0
    items = value.get("items")
    if not isinstance(items, dict):
        return [f"{label}: confidence_score.items must be a mapping"], 0.0
    errors: list[str] = []
    score = 0.0
    for key, points in CONFIDENCE_ITEMS.items():
        item_label = f"{label}: confidence_score.items.{key}"
        item = items.get(key)
        if not isinstance(item, dict):
            errors.append(f"{item_label} must be a mapping")
            continue
        present = item.get("present")
        if not isinstance(present, bool):
            errors.append(f"{item_label}.present must be true or false")
            continue
        if item.get("points") != points:
            errors.append(f"{item_label}.points must be {points}")
        if present:
            score += points
            if not str(item.get("evidence_note", "")).strip():
                errors.append(f"{item_label}.evidence_note is required when present")
    return errors, score


def _validate_overclaim_risk(value: Any, status: Any, label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label}: overclaim_risk must be a mapping"]
    errors: list[str] = []
    level = value.get("level")
    if level not in VALID_RISK_LEVELS:
        errors.append(f"{label}: overclaim_risk.level must be one of {sorted(VALID_RISK_LEVELS)}")
    if status != "not_started" and level == "not_evaluated":
        errors.append(f"{label}: overclaim_risk.level cannot be not_evaluated after scoring starts")
    checklist = value.get("checklist")
    if not isinstance(checklist, dict):
        return errors + [f"{label}: overclaim_risk.checklist must be a mapping"]
    yes_count = 0
    for key in OVERCLAIM_CHECKS:
        entry_label = f"{label}: overclaim_risk.checklist.{key}"
        entry = checklist.get(key)
        if not isinstance(entry, dict):
            errors.append(f"{entry_label} must be a mapping")
            continue
        yes = entry.get("yes")
        if not isinstance(yes, bool):
            errors.append(f"{entry_label}.yes must be true or false")
            continue
        if yes:
            yes_count += 1
            if not str(entry.get("evidence_note", "")).strip():
                errors.append(f"{entry_label}.evidence_note is required when yes")
    if yes_count >= 3 and level not in {"high", "critical"}:
        errors.append(f"{label}: overclaim_risk.level must be high or critical when checklist yes_count >= 3")
    return errors


def _validate_reproducibility_risk(value: Any, status: Any, label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label}: reproducibility_risk must be a mapping"]
    level = value.get("level")
    errors: list[str] = []
    if level not in VALID_RISK_LEVELS:
        errors.append(f"{label}: reproducibility_risk.level must be one of {sorted(VALID_RISK_LEVELS)}")
    if status != "not_started" and level == "not_evaluated":
        errors.append(f"{label}: reproducibility_risk.level cannot be not_evaluated after scoring starts")
    if status != "not_started" and not str(value.get("evidence_note", "")).strip():
        errors.append(f"{label}: reproducibility_risk.evidence_note is required after scoring starts")
    return errors


def _validate_reviewer_consistency(value: Any, label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label}: reviewer_consistency must be a mapping"]
    errors: list[str] = []
    count = value.get("reviewer_count")
    if not isinstance(count, int) or count < 0:
        errors.append(f"{label}: reviewer_consistency.reviewer_count must be a non-negative integer")
    requires = value.get("requires_adjudication")
    if not isinstance(requires, bool):
        errors.append(f"{label}: reviewer_consistency.requires_adjudication must be true or false")
    if requires and not str(value.get("disagreement_note", "")).strip():
        errors.append(f"{label}: reviewer_consistency.disagreement_note is required when adjudication is required")
    return errors


def _valid_coefficient(value: Any) -> bool:
    return isinstance(value, (int, float)) and float(value) in VALID_COEFFICIENTS


def _same_number(actual: Any, expected: float) -> bool:
    if not isinstance(actual, (int, float)):
        return False
    return abs(float(actual) - float(expected)) < 1e-9


def _fmt(value: float) -> int | float:
    if abs(value - round(value)) < 1e-9:
        return int(round(value))
    return round(value, 4)


def _rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)
