"""Weekly Paper Lab structure validation.

The paper lab is a research-training input to Idea OS. It keeps paper reading,
minimum reproduction, failure notes, and research-question seeds in a separate
workspace before anything becomes a canonical idea YAML record.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from idea_os.paper_quality import validate_quality_evaluation_file
from idea_os.store import REPO_ROOT
from idea_os.yaml_io import load_yaml


LAB_DIR = "weekly-paper-lab"
PAPERS_DIR = "papers"
ARTIFACT_ROOT_PREFIX = "/home/jnln3799/research-artifacts/weekly-paper-lab/"

EXPECTED_MARKDOWN_FILES = [
    "00_metadata.md",
    "01_problem.md",
    "02_method_breakdown.md",
    "03_key_figures.md",
    "04_rtx5080_implementation_log.md",
    "05_bottleneck_and_question.md",
    "06_research_idea_seed.md",
    "07_scoring_report.md",
    "08_scientific_evaluation.md",
]

REQUIRED_SCORING_REPORT_SECTIONS = [
    "## Shortlist Triage Scoring",
    "## Candidate Selection Explanation",
    "## Idea Connection Scoring",
    "## Synthesis Scoring",
    "## Evidence Gaps And Overrides",
]

REQUIRED_PAPER_FIELDS = [
    "paper_id",
    "week",
    "cycle_slot",
    "domain_type",
    "title",
    "source_urls",
    "triage_score",
    "reproduction_level",
    "rtx5080_experiment",
    "failure_taxonomy",
    "research_question_seed",
    "idea_links",
    "idea_connections",
    "synthesis_assessment",
    "project_links",
    "planning_sync",
]

VALID_CYCLE_SLOTS = {"main_a", "main_b", "cross_domain"}
VALID_DOMAIN_TYPES = {"ai_agent_llm_cybersecurity", "cross_domain"}
VALID_PLANNING_SYNC_STATUS = {"not_synced", "synced", "blocked", "not_needed"}
VALID_RESEARCH_ACTIONS = {"none", "create_idea", "update_idea", "park", "kill", "graduate"}
VALID_RELATIONSHIP_TYPES = {
    "method_reference",
    "evaluation_fixture",
    "implementation_context",
    "risk_reference",
    "baseline_reference",
    "synthesis_seed",
}
VALID_REFERENCE_ROLES = {
    "method_reference",
    "background_reference",
    "baseline_reference",
    "evaluation_reference",
    "risk_reference",
    "not_ready",
}

CONNECTION_RULE_VERSION = "paper_connection_rubric_v2"
SYNTHESIS_RULE_VERSION = "paper_synthesis_rubric_v1"

CONNECTION_DIMENSION_RULES: dict[str, dict[str, tuple[str, int, int | None]]] = {
    "topical_alignment": {
        "title_keyword_overlaps": ("list_count", 2, 8),
        "shared_tags": ("list_count", 2, 8),
        "explicit_topic_match": ("bool", 4, None),
    },
    "method_workflow_alignment": {
        "shared_methods": ("list_count", 4, 8),
        "shared_workflow_stages": ("list_count", 3, 6),
        "same_artifact_type": ("bool", 3, None),
        "same_failure_mode": ("bool", 3, None),
    },
    "next_step_impact": {
        "directly_updates_next_step": ("bool", 8, None),
        "produces_required_artifact": ("bool", 5, None),
        "reduces_open_uncertainties": ("list_count", 2, 4),
        "actionable_within_one_week": ("bool", 3, None),
    },
    "metric_baseline_support": {
        "shared_metrics": ("list_count", 3, 6),
        "provides_baseline": ("bool", 5, None),
        "provides_fixture": ("bool", 5, None),
        "measurable_success_condition": ("bool", 4, None),
    },
    "research_generation_value": {
        "new_tests": ("list_count", 4, 8),
        "synthesis_paths": ("list_count", 3, 6),
        "can_update_yaml_record": ("bool", 3, None),
        "can_be_reference_citation": ("bool", 3, None),
    },
}

SYNTHESIS_EVIDENCE_POINTS = {
    "has_transferable_method": 5,
    "has_measurable_fixture": 5,
    "links_two_or_more_ideas": 4,
    "defines_new_baseline_or_metric": 3,
    "can_be_cited_as_reference": 3,
}

PAPER_FOLDER_RE = re.compile(r"^\d{4}-W\d{2}-[a-z0-9][a-z0-9-]*$")
WEEK_RE = re.compile(r"^\d{4}-W\d{2}$")


def paper_lab_path(root: str | Path | None = None) -> Path:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    return repo / LAB_DIR


def paper_folders(root: str | Path | None = None) -> list[Path]:
    papers = paper_lab_path(root) / PAPERS_DIR
    if not papers.exists():
        return []
    return sorted(path for path in papers.iterdir() if path.is_dir())


def validate_paper_lab(root: str | Path | None = None) -> list[str]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    lab = paper_lab_path(repo)
    errors: list[str] = []
    if not lab.exists():
        return [f"missing {LAB_DIR}/"]
    papers = lab / PAPERS_DIR
    if not papers.exists():
        errors.append(f"missing {LAB_DIR}/{PAPERS_DIR}/")
        return errors
    for folder in paper_folders(repo):
        errors.extend(validate_paper_folder(folder, repo))
    return errors


def validate_paper_folder(folder: str | Path, root: str | Path | None = None) -> list[str]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    paper_dir = Path(folder).resolve()
    errors: list[str] = []
    label = _rel(paper_dir, repo)

    if not PAPER_FOLDER_RE.match(paper_dir.name):
        errors.append(f"{label}: folder name must match YYYY-Www-slug")

    yaml_path = paper_dir / "paper.yaml"
    if not yaml_path.exists():
        errors.append(f"{label}: missing paper.yaml")
    else:
        try:
            data = load_yaml(yaml_path)
        except Exception as exc:
            errors.append(f"{_rel(yaml_path, repo)}: could not parse YAML: {exc}")
        else:
            if not isinstance(data, dict):
                errors.append(f"{_rel(yaml_path, repo)}: paper.yaml must be a mapping")
            else:
                errors.extend(validate_paper_record(data, paper_dir, repo))

    for filename in EXPECTED_MARKDOWN_FILES:
        path = paper_dir / filename
        if not path.exists():
            errors.append(f"{label}: missing {filename}")
        elif filename == "07_scoring_report.md":
            errors.extend(_validate_scoring_report(path, repo))
    expected_id = None
    if yaml_path.exists():
        try:
            expected_id = str(load_yaml(yaml_path).get("paper_id", ""))
        except Exception:
            expected_id = None
    errors.extend(validate_quality_evaluation_file(paper_dir / "scientific_evaluation.yaml", repo, expected_id))
    return errors


def validate_paper_record(data: dict[str, Any], paper_dir: str | Path, root: str | Path | None = None) -> list[str]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    path_label = _rel(Path(paper_dir).resolve() / "paper.yaml", repo)
    errors: list[str] = []

    for field in REQUIRED_PAPER_FIELDS:
        if field not in data:
            errors.append(f"{path_label}: missing field: {field}")

    week = str(data.get("week", "")).strip()
    if week and not WEEK_RE.match(week):
        errors.append(f"{path_label}: week must match YYYY-Www")

    folder_week = Path(paper_dir).name[:8]
    if week and WEEK_RE.match(week) and folder_week != week:
        errors.append(f"{path_label}: week must match folder prefix {folder_week}")

    if data.get("cycle_slot") not in VALID_CYCLE_SLOTS:
        errors.append(f"{path_label}: cycle_slot must be one of {sorted(VALID_CYCLE_SLOTS)}")

    if data.get("domain_type") not in VALID_DOMAIN_TYPES:
        errors.append(f"{path_label}: domain_type must be one of {sorted(VALID_DOMAIN_TYPES)}")

    source_urls = data.get("source_urls")
    if not isinstance(source_urls, list) or not any(str(url).strip() for url in source_urls):
        errors.append(f"{path_label}: source_urls must be a non-empty list")

    errors.extend(_validate_triage_score(data.get("triage_score"), path_label))
    errors.extend(_validate_reproduction_level(data.get("reproduction_level"), path_label))
    errors.extend(_validate_rtx5080_experiment(data.get("rtx5080_experiment"), path_label))
    errors.extend(_validate_failure_taxonomy(data.get("failure_taxonomy"), path_label))
    errors.extend(_validate_research_question_seed(data.get("research_question_seed"), path_label))
    errors.extend(_validate_idea_connections(data.get("idea_connections"), data.get("idea_links"), path_label))
    errors.extend(_validate_synthesis_assessment(data.get("synthesis_assessment"), data.get("idea_links"), path_label))

    for list_field in ["idea_links", "project_links"]:
        if list_field in data and not isinstance(data.get(list_field), list):
            errors.append(f"{path_label}: {list_field} must be a list")

    planning_sync = data.get("planning_sync")
    if not isinstance(planning_sync, dict):
        errors.append(f"{path_label}: planning_sync must be a mapping")
    else:
        status = planning_sync.get("status")
        if status not in VALID_PLANNING_SYNC_STATUS:
            errors.append(f"{path_label}: planning_sync.status must be one of {sorted(VALID_PLANNING_SYNC_STATUS)}")
        if not str(planning_sync.get("canonical_path", "")).strip():
            errors.append(f"{path_label}: planning_sync.canonical_path is required")
        linked = planning_sync.get("linked_idea_ids", [])
        if linked is not None and not isinstance(linked, list):
            errors.append(f"{path_label}: planning_sync.linked_idea_ids must be a list")

    return errors


def _validate_scoring_report(path: Path, root: Path) -> list[str]:
    label = _rel(path, root)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{label}: could not read scoring report: {exc}"]

    errors = []
    if len(text.strip()) < 200:
        errors.append(f"{label}: scoring report must explain why the scores were assigned")
    for section in REQUIRED_SCORING_REPORT_SECTIONS:
        if section not in text:
            errors.append(f"{label}: missing scoring report section: {section}")
    return errors


def _validate_triage_score(value: Any, path_label: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, dict):
        return [f"{path_label}: triage_score must be a mapping"]
    total = value.get("total")
    if not isinstance(total, int) or total < 0 or total > 100:
        errors.append(f"{path_label}: triage_score.total must be an integer from 0 to 100")
    expected_dimensions = [
        "recency_discussion",
        "idea_os_connection",
        "rtx5080_feasibility",
        "code_data_benchmark",
        "research_question_potential",
    ]
    for key in expected_dimensions:
        if key in value and not _valid_dimension_score(value[key]):
            errors.append(f"{path_label}: triage_score.{key} must be an integer from 0 to 20")
    cross = value.get("cross_domain_transfer")
    if cross is not None and not _valid_dimension_score(cross):
        errors.append(f"{path_label}: triage_score.cross_domain_transfer must be an integer from 0 to 20")
    return errors


def _validate_reproduction_level(value: Any, path_label: str) -> list[str]:
    if isinstance(value, dict):
        level = value.get("level")
    else:
        level = value
    if not isinstance(level, int) or level < 1 or level > 5:
        return [f"{path_label}: reproduction_level.level must be an integer from 1 to 5"]
    return []


def _validate_rtx5080_experiment(value: Any, path_label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{path_label}: rtx5080_experiment must be a mapping"]
    errors: list[str] = []
    artifact_root = str(value.get("artifact_root", "")).strip()
    if artifact_root and not artifact_root.startswith(ARTIFACT_ROOT_PREFIX):
        errors.append(f"{path_label}: rtx5080_experiment.artifact_root should be under {ARTIFACT_ROOT_PREFIX}")
    if not str(value.get("minimum_viable_experiment", "")).strip():
        errors.append(f"{path_label}: rtx5080_experiment.minimum_viable_experiment is required")
    return errors


def _validate_failure_taxonomy(value: Any, path_label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{path_label}: failure_taxonomy must be a mapping"]
    expected = ["engineering", "data", "evaluation", "theory", "hardware", "environment", "cost", "problem_definition"]
    errors = []
    for key in expected:
        if key in value and not isinstance(value[key], list):
            errors.append(f"{path_label}: failure_taxonomy.{key} must be a list")
    return errors


def _validate_research_question_seed(value: Any, path_label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{path_label}: research_question_seed must be a mapping"]
    errors = []
    action = value.get("next_idea_action")
    if action not in VALID_RESEARCH_ACTIONS:
        errors.append(f"{path_label}: research_question_seed.next_idea_action must be one of {sorted(VALID_RESEARCH_ACTIONS)}")
    if action in {"create_idea", "update_idea", "graduate"} and not str(value.get("question", "")).strip():
        errors.append(f"{path_label}: research_question_seed.question is required when action is {action}")
    return errors


def _validate_idea_connections(value: Any, idea_links: Any, path_label: str) -> list[str]:
    if not isinstance(value, list) or not value:
        return [f"{path_label}: idea_connections must be a non-empty list"]

    errors: list[str] = []
    connected_ids: list[str] = []
    for index, connection in enumerate(value, start=1):
        label = f"{path_label}: idea_connections[{index}]"
        if not isinstance(connection, dict):
            errors.append(f"{label} must be a mapping")
            continue

        idea_id = str(connection.get("idea_id", "")).strip()
        if not idea_id:
            errors.append(f"{label}.idea_id is required")
        else:
            connected_ids.append(idea_id)
        if not str(connection.get("idea_path", "")).strip():
            errors.append(f"{label}.idea_path is required")
        if connection.get("relationship_type") not in VALID_RELATIONSHIP_TYPES:
            errors.append(f"{label}.relationship_type must be one of {sorted(VALID_RELATIONSHIP_TYPES)}")
        if not str(connection.get("expected_use", "")).strip():
            errors.append(f"{label}.expected_use is required")

        strength = connection.get("connection_strength")
        if not isinstance(strength, dict):
            errors.append(f"{label}.connection_strength must be a mapping")
            continue
        if strength.get("rule_version") != CONNECTION_RULE_VERSION:
            errors.append(f"{label}.connection_strength.rule_version must be {CONNECTION_RULE_VERSION}")
        dimension_errors, expected = _validate_connection_dimensions(strength, label)
        errors.extend(dimension_errors)
        if strength.get("score") != expected:
            errors.append(f"{label}.connection_strength.score must be {expected}")

    if isinstance(idea_links, list):
        missing = sorted(set(str(idea_id) for idea_id in idea_links) - set(connected_ids))
        if missing:
            errors.append(f"{path_label}: idea_connections missing idea_links {missing}")
    return errors


def _validate_connection_dimensions(strength: dict[str, Any], label: str) -> tuple[list[str], int]:
    errors: list[str] = []
    dimensions = strength.get("dimensions")
    if not isinstance(dimensions, dict):
        return [f"{label}.connection_strength.dimensions must be a mapping"], 0

    total = 0
    for dimension, rules in CONNECTION_DIMENSION_RULES.items():
        dimension_label = f"{label}.connection_strength.dimensions.{dimension}"
        value = dimensions.get(dimension)
        if not isinstance(value, dict):
            errors.append(f"{dimension_label} must be a mapping")
            continue
        evidence = value.get("evidence")
        if not isinstance(evidence, dict):
            errors.append(f"{dimension_label}.evidence must be a mapping")
            continue
        dimension_score = 0
        for field, rule in rules.items():
            kind, points, cap = rule
            if field not in evidence:
                errors.append(f"{dimension_label}.evidence.{field} is required")
                continue
            field_value = evidence[field]
            if kind == "bool":
                if not isinstance(field_value, bool):
                    errors.append(f"{dimension_label}.evidence.{field} must be true or false")
                    continue
                if field_value:
                    dimension_score += points
            elif kind == "list_count":
                if not isinstance(field_value, list):
                    errors.append(f"{dimension_label}.evidence.{field} must be a list")
                    continue
                if not all(str(item).strip() for item in field_value):
                    errors.append(f"{dimension_label}.evidence.{field} must contain only non-empty items")
                    continue
                raw_score = len(field_value) * points
                dimension_score += min(raw_score, int(cap or raw_score))
        dimension_score = min(20, dimension_score)
        total += dimension_score
        if value.get("score") != dimension_score:
            errors.append(f"{dimension_label}.score must be {dimension_score}")
    return errors, min(100, total)


def _validate_synthesis_assessment(value: Any, idea_links: Any, path_label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{path_label}: synthesis_assessment must be a mapping"]
    errors: list[str] = []
    if value.get("rule_version") != SYNTHESIS_RULE_VERSION:
        errors.append(f"{path_label}: synthesis_assessment.rule_version must be {SYNTHESIS_RULE_VERSION}")
    if value.get("reference_role") not in VALID_REFERENCE_ROLES:
        errors.append(f"{path_label}: synthesis_assessment.reference_role must be one of {sorted(VALID_REFERENCE_ROLES)}")
    if not str(value.get("candidate_research_method", "")).strip():
        errors.append(f"{path_label}: synthesis_assessment.candidate_research_method is required")
    combine_ids = value.get("combine_with_idea_ids")
    if not isinstance(combine_ids, list) or not combine_ids:
        errors.append(f"{path_label}: synthesis_assessment.combine_with_idea_ids must be a non-empty list")
    elif isinstance(idea_links, list):
        missing = sorted(set(str(idea_id) for idea_id in combine_ids) - set(str(idea_id) for idea_id in idea_links))
        if missing:
            errors.append(f"{path_label}: synthesis_assessment.combine_with_idea_ids must be included in idea_links: {missing}")

    evidence = value.get("evidence")
    if not isinstance(evidence, dict):
        errors.append(f"{path_label}: synthesis_assessment.evidence must be a mapping")
    else:
        for field in SYNTHESIS_EVIDENCE_POINTS:
            if field not in evidence:
                errors.append(f"{path_label}: synthesis_assessment.evidence.{field} is required")
            elif not isinstance(evidence[field], bool):
                errors.append(f"{path_label}: synthesis_assessment.evidence.{field} must be true or false")
        expected = _score_evidence(evidence, SYNTHESIS_EVIDENCE_POINTS)
        if value.get("synthesis_score") != expected:
            errors.append(f"{path_label}: synthesis_assessment.synthesis_score must be {expected}")

    followups = value.get("required_followups")
    if followups is not None and not isinstance(followups, list):
        errors.append(f"{path_label}: synthesis_assessment.required_followups must be a list")
    return errors


def _score_evidence(evidence: dict[str, Any], points: dict[str, int]) -> int:
    return min(20, sum(score for field, score in points.items() if evidence.get(field) is True))


def _valid_dimension_score(value: Any) -> bool:
    return isinstance(value, int) and 0 <= value <= 20


def _rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)
