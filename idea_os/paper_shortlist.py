"""Auditable weekly paper shortlist scoring.

Shortlists are evidence-first: candidate scores are derived from fixed boolean
evidence fields, capped by rubric dimensions, and recomputed by validation.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from idea_os.paper_lab import LAB_DIR, VALID_CYCLE_SLOTS, paper_lab_path
from idea_os.store import REPO_ROOT
from idea_os.yaml_io import load_yaml


RUBRIC_VERSION = "paper_lab_rubric_v1"
SHORTLISTS_DIR = "shortlists"
WEEK_RE = re.compile(r"^\d{4}-W\d{2}$")
ARXIV_VERSION_RE = re.compile(r"v\d+$", re.IGNORECASE)

BASE_DIMENSIONS = [
    "recency_discussion",
    "idea_os_connection",
    "rtx5080_feasibility",
    "code_data_benchmark",
    "research_question_potential",
]

MAIN_SLOT_NOVELTY_DIMENSION = "novelty_or_transfer"
CROSS_DOMAIN_DIMENSION = "cross_domain_transfer"

DIMENSION_RULES: dict[str, dict[str, int]] = {
    "recency_discussion": {
        "published_within_30_days": 5,
        "published_within_90_days": 3,
        "hf_trending_present": 5,
        "github_stars_100_plus": 3,
        "github_stars_500_plus": 5,
        "social_discussion_present": 3,
        "benchmark_or_leaderboard_mentioned": 4,
    },
    "idea_os_connection": {
        "matches_existing_project": 6,
        "matches_existing_research_thread": 5,
        "matches_existing_idea_yaml": 5,
        "can_update_existing_method": 3,
        "only_general_interest": 1,
    },
    "rtx5080_feasibility": {
        "official_code_available": 4,
        "single_gpu_possible": 4,
        "fits_16gb_or_24gb_vram": 4,
        "small_dataset_or_fixture_possible": 3,
        "runtime_under_4_hours": 3,
        "docker_or_conda_install_clear": 2,
    },
    "code_data_benchmark": {
        "official_code": 5,
        "unofficial_code": 3,
        "dataset_available": 4,
        "benchmark_available": 4,
        "clear_metrics": 3,
        "reproducible_commands_or_demo": 4,
    },
    "research_question_potential": {
        "has_explicit_limitation_section": 4,
        "has_failure_cases": 4,
        "has_evaluation_gap": 4,
        "has_deployment_gap": 3,
        "has_theory_or_mechanism_gap": 3,
        "can_generate_3_questions": 2,
    },
    "novelty_or_transfer": {
        "not_duplicate_of_recent_lab_pick": 5,
        "introduces_new_problem_frame": 5,
        "introduces_new_method_family": 5,
        "has_transfer_path_to_other_domain": 5,
    },
    "cross_domain_transfer": {
        "method_transferable_to_ai_agent": 5,
        "method_transferable_to_cybersecurity": 5,
        "method_transferable_to_human_ai_workflow": 5,
        "can_design_analogy_experiment": 5,
    },
}

PICK_WEIGHTS = {
    "research_question_potential": 0.25,
    "rtx5080_feasibility": 0.20,
    "idea_os_connection": 0.20,
    "code_data_benchmark": 0.15,
    "recency_discussion": 0.10,
    "novelty_or_transfer": 0.10,
}


def shortlist_paths(root: str | Path | None = None) -> list[Path]:
    shortlists = paper_lab_path(root) / SHORTLISTS_DIR
    if not shortlists.exists():
        return []
    return sorted(shortlists.glob("*.yaml"))


def validate_shortlists(root: str | Path | None = None) -> list[str]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    lab = repo / LAB_DIR
    errors: list[str] = []
    if not lab.exists():
        return [f"missing {LAB_DIR}/"]
    for path in shortlist_paths(repo):
        errors.extend(validate_shortlist_file(path, repo))
    return errors


def validate_shortlist_file(path: str | Path, root: str | Path | None = None) -> list[str]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    shortlist_path = Path(path).resolve()
    label = _rel(shortlist_path, repo)
    errors: list[str] = []

    try:
        data = load_yaml(shortlist_path)
    except Exception as exc:
        return [f"{label}: could not parse YAML: {exc}"]
    if not isinstance(data, dict):
        return [f"{label}: shortlist must be a mapping"]

    week = str(data.get("week", "")).strip()
    if not WEEK_RE.match(week):
        errors.append(f"{label}: week must match YYYY-Www")
    elif shortlist_path.stem != week:
        errors.append(f"{label}: filename must match week {week}.yaml")

    if data.get("rubric_version") != RUBRIC_VERSION:
        errors.append(f"{label}: rubric_version must be {RUBRIC_VERSION}")

    cycle_slot = data.get("cycle_slot")
    if cycle_slot not in VALID_CYCLE_SLOTS:
        errors.append(f"{label}: cycle_slot must be one of {sorted(VALID_CYCLE_SLOTS)}")

    candidates = data.get("candidates")
    if not isinstance(candidates, list) or len(candidates) < 3:
        errors.append(f"{label}: candidates must contain at least 3 papers")
        return errors
    if len(candidates) > 5:
        errors.append(f"{label}: candidates should contain at most 5 papers")

    prior_selected = selected_item_registry(repo, before_week=week)
    seen_candidates: dict[str, str] = {}
    selected_count = 0
    for index, candidate in enumerate(candidates, start=1):
        if not isinstance(candidate, dict):
            errors.append(f"{label}: candidate {index} must be a mapping")
            continue
        candidate_label = f"{label}: candidate {index} {candidate.get('paper_id', '')}".rstrip()
        if candidate.get("selected") is True:
            selected_count += 1
        errors.extend(validate_candidate(candidate, cycle_slot, candidate_label))
        errors.extend(_validate_not_previously_selected(candidate, prior_selected, candidate_label))
        errors.extend(_validate_unique_candidate(candidate, seen_candidates, candidate_label))

    if selected_count != 1:
        errors.append(f"{label}: exactly one candidate must have selected: true")
    return errors


def selected_item_registry(root: str | Path | None = None, before_week: str | None = None) -> list[dict[str, Any]]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    registry: list[dict[str, Any]] = []

    papers_dir = paper_lab_path(repo) / "papers"
    if papers_dir.exists():
        for paper_yaml in sorted(papers_dir.glob("*/paper.yaml")):
            try:
                data = load_yaml(paper_yaml)
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            week = str(data.get("week", "")).strip()
            if not _is_before_week(week, before_week):
                continue
            registry.append(
                _registry_item(
                    paper_id=data.get("paper_id"),
                    title=data.get("title"),
                    urls=data.get("source_urls"),
                    week=week,
                    path=_rel(paper_yaml, repo),
                    source="paper_record",
                )
            )

    for shortlist in shortlist_paths(repo):
        try:
            data = load_yaml(shortlist)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        week = str(data.get("week", "")).strip()
        if not _is_before_week(week, before_week):
            continue
        candidates = data.get("candidates")
        if not isinstance(candidates, list):
            continue
        for candidate in candidates:
            if not isinstance(candidate, dict) or candidate.get("selected") is not True:
                continue
            registry.append(
                _registry_item(
                    paper_id=candidate.get("paper_id"),
                    title=candidate.get("title"),
                    urls=_candidate_urls(candidate),
                    week=week,
                    path=_rel(shortlist, repo),
                    source="shortlist_selected",
                )
            )
    return registry


def validate_candidate(candidate: dict[str, Any], cycle_slot: Any, label: str) -> list[str]:
    errors: list[str] = []
    for field in ["paper_id", "title", "selected", "evidence_sources", "scores", "candidate_score", "weekly_pick_score"]:
        if field not in candidate:
            errors.append(f"{label}: missing field: {field}")

    selected = candidate.get("selected")
    if not isinstance(selected, bool):
        errors.append(f"{label}: selected must be true or false")
    if selected is True and not str(candidate.get("selection_reason", "")).strip():
        errors.append(f"{label}: selection_reason is required for selected paper")
    if selected is False and not str(candidate.get("rejected_reason", "")).strip():
        errors.append(f"{label}: rejected_reason is required for rejected paper")

    errors.extend(_validate_sources(candidate.get("evidence_sources"), label))

    scores = candidate.get("scores")
    if not isinstance(scores, dict):
        errors.append(f"{label}: scores must be a mapping")
        return errors

    needed = list(BASE_DIMENSIONS)
    if cycle_slot == "cross_domain":
        needed.append(CROSS_DOMAIN_DIMENSION)
    else:
        needed.append(MAIN_SLOT_NOVELTY_DIMENSION)

    computed: dict[str, int] = {}
    for dimension in needed:
        if dimension not in scores:
            errors.append(f"{label}: scores.{dimension} is required")
            continue
        dimension_errors, score = validate_dimension_score(scores[dimension], dimension, label)
        errors.extend(dimension_errors)
        computed[dimension] = score

    errors.extend(_validate_mutual_exclusion(scores, label))

    if len([dimension for dimension in BASE_DIMENSIONS if dimension in computed]) == len(BASE_DIMENSIONS):
        expected_candidate = candidate_score(computed)
        if candidate.get("candidate_score") != expected_candidate:
            errors.append(f"{label}: candidate_score must be {expected_candidate}")

    novelty_dimension = CROSS_DOMAIN_DIMENSION if cycle_slot == "cross_domain" else MAIN_SLOT_NOVELTY_DIMENSION
    if all(dimension in computed for dimension in BASE_DIMENSIONS + [novelty_dimension]):
        expected_pick = weekly_pick_score(computed, novelty_dimension)
        if _as_float(candidate.get("weekly_pick_score")) != expected_pick:
            errors.append(f"{label}: weekly_pick_score must be {expected_pick}")

    return errors


def validate_dimension_score(value: Any, dimension: str, label: str) -> tuple[list[str], int]:
    errors: list[str] = []
    if not isinstance(value, dict):
        return [f"{label}: scores.{dimension} must be a mapping"], 0
    if value.get("rule_version") != RUBRIC_VERSION:
        errors.append(f"{label}: scores.{dimension}.rule_version must be {RUBRIC_VERSION}")
    evidence = value.get("evidence")
    if not isinstance(evidence, dict):
        return errors + [f"{label}: scores.{dimension}.evidence must be a mapping"], 0

    for key in DIMENSION_RULES[dimension]:
        if key not in evidence:
            errors.append(f"{label}: scores.{dimension}.evidence.{key} is required")
        elif not isinstance(evidence[key], bool):
            errors.append(f"{label}: scores.{dimension}.evidence.{key} must be true or false")

    expected = score_dimension(dimension, evidence)
    if value.get("score") != expected:
        errors.append(f"{label}: scores.{dimension}.score must be {expected}")
    return errors, expected


def score_dimension(dimension: str, evidence: dict[str, Any]) -> int:
    raw = 0
    for field, points in DIMENSION_RULES[dimension].items():
        if evidence.get(field) is True:
            raw += points
    return min(20, raw)


def candidate_score(scores: dict[str, int]) -> int:
    return sum(int(scores.get(dimension, 0)) for dimension in BASE_DIMENSIONS)


def weekly_pick_score(scores: dict[str, int], novelty_dimension: str) -> float:
    weighted = (
        PICK_WEIGHTS["research_question_potential"] * scores.get("research_question_potential", 0)
        + PICK_WEIGHTS["rtx5080_feasibility"] * scores.get("rtx5080_feasibility", 0)
        + PICK_WEIGHTS["idea_os_connection"] * scores.get("idea_os_connection", 0)
        + PICK_WEIGHTS["code_data_benchmark"] * scores.get("code_data_benchmark", 0)
        + PICK_WEIGHTS["recency_discussion"] * scores.get("recency_discussion", 0)
        + PICK_WEIGHTS["novelty_or_transfer"] * scores.get(novelty_dimension, 0)
    )
    return round(weighted * 5, 2)


def _validate_sources(value: Any, label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label}: evidence_sources must be a mapping"]
    errors = []
    if not str(value.get("paper_url", "")).strip():
        errors.append(f"{label}: evidence_sources.paper_url is required")
    if not str(value.get("checked_at", "")).strip():
        errors.append(f"{label}: evidence_sources.checked_at is required")
    return errors


def _validate_mutual_exclusion(scores: dict[str, Any], label: str) -> list[str]:
    errors = []
    idea = scores.get("idea_os_connection", {})
    if isinstance(idea, dict) and isinstance(idea.get("evidence"), dict):
        evidence = idea["evidence"]
        strong = [
            "matches_existing_project",
            "matches_existing_research_thread",
            "matches_existing_idea_yaml",
            "can_update_existing_method",
        ]
        if evidence.get("only_general_interest") is True and any(evidence.get(key) is True for key in strong):
            errors.append(f"{label}: only_general_interest cannot be true with stronger Idea OS connection evidence")

    code = scores.get("code_data_benchmark", {})
    if isinstance(code, dict) and isinstance(code.get("evidence"), dict):
        evidence = code["evidence"]
        if evidence.get("official_code") is True and evidence.get("unofficial_code") is True:
            errors.append(f"{label}: official_code and unofficial_code should not both be true")
    return errors


def _validate_not_previously_selected(candidate: dict[str, Any], registry: list[dict[str, Any]], label: str) -> list[str]:
    matches = _previous_selection_matches(candidate, registry)
    if not matches:
        return []
    first = matches[0]
    reason = first["reason"]
    return [
        (
            f"{label}: already selected before; repeated papers or essays are excluded "
            f"from new shortlists ({reason} matched {first['path']})"
        )
    ]


def _validate_unique_candidate(candidate: dict[str, Any], seen: dict[str, str], label: str) -> list[str]:
    errors: list[str] = []
    for key in _candidate_identity_keys(candidate):
        previous = seen.get(key)
        if previous:
            errors.append(f"{label}: duplicates another candidate in this shortlist ({key} matched {previous})")
        else:
            seen[key] = label
    return errors


def _previous_selection_matches(candidate: dict[str, Any], registry: list[dict[str, Any]]) -> list[dict[str, str]]:
    candidate_id = _normalize_text(candidate.get("paper_id"))
    candidate_title = _normalize_title(candidate.get("title"))
    candidate_urls = set(_candidate_urls(candidate))
    matches: list[dict[str, str]] = []

    for item in registry:
        if candidate_id and candidate_id == item.get("paper_id"):
            matches.append({"path": str(item["path"]), "reason": f"paper_id {candidate_id}"})
            continue
        if candidate_title and candidate_title == item.get("title"):
            matches.append({"path": str(item["path"]), "reason": f"title {candidate_title}"})
            continue
        overlap = candidate_urls.intersection(set(item.get("urls", [])))
        if overlap:
            matches.append({"path": str(item["path"]), "reason": f"url {sorted(overlap)[0]}"})
    return matches


def _candidate_identity_keys(candidate: dict[str, Any]) -> list[str]:
    keys: list[str] = []
    paper_id = _normalize_text(candidate.get("paper_id"))
    title = _normalize_title(candidate.get("title"))
    if paper_id:
        keys.append(f"paper_id:{paper_id}")
    if title:
        keys.append(f"title:{title}")
    keys.extend(f"url:{url}" for url in _candidate_urls(candidate))
    return keys


def _registry_item(
    paper_id: Any,
    title: Any,
    urls: Any,
    week: str,
    path: str,
    source: str,
) -> dict[str, Any]:
    return {
        "paper_id": _normalize_text(paper_id),
        "title": _normalize_title(title),
        "urls": _identity_urls(urls),
        "week": week,
        "path": path,
        "source": source,
    }


def _candidate_urls(candidate: dict[str, Any]) -> list[str]:
    sources = candidate.get("evidence_sources")
    if not isinstance(sources, dict):
        return []
    url_fields = [
        "paper_url",
        "doi_url",
        "arxiv_url",
        "hf_trending_url",
        "openalex_url",
        "publisher_url",
        "essay_url",
    ]
    return _identity_urls([sources.get(field) for field in url_fields])


def _identity_urls(value: Any) -> list[str]:
    if isinstance(value, str):
        urls = [value]
    elif isinstance(value, list):
        urls = [item for item in value if isinstance(item, str)]
    else:
        urls = []

    normalized = [_normalize_url(url) for url in urls]
    normalized = [url for url in normalized if url]
    identity_urls = [url for url in normalized if not _is_code_or_data_url(url)]
    return sorted(set(identity_urls or normalized))


def _normalize_url(value: Any) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    parts = urlsplit(raw)
    if not parts.scheme or not parts.netloc:
        return raw.rstrip("/").lower()

    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    path = re.sub(r"/+", "/", parts.path).rstrip("/")

    if netloc.endswith("arxiv.org"):
        path = path.replace("/pdf/", "/abs/", 1)
        if path.endswith(".pdf"):
            path = path[:-4]
        path = ARXIV_VERSION_RE.sub("", path)

    return urlunsplit((scheme, netloc, path, "", ""))


def _is_code_or_data_url(url: str) -> bool:
    host = urlsplit(url).netloc.lower()
    code_or_data_hosts = {
        "github.com",
        "www.github.com",
        "gitlab.com",
        "www.gitlab.com",
        "bitbucket.org",
        "www.bitbucket.org",
        "kaggle.com",
        "www.kaggle.com",
    }
    return host in code_or_data_hosts


def _normalize_text(value: Any) -> str:
    return str(value or "").strip().lower()


def _normalize_title(value: Any) -> str:
    text = re.sub(r"[^a-z0-9]+", " ", _normalize_text(value))
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) >= 12 else ""


def _is_before_week(week: str, before_week: str | None) -> bool:
    if not WEEK_RE.match(str(week or "")):
        return before_week is None
    if before_week is None or not WEEK_RE.match(before_week):
        return True
    return week < before_week


def _as_float(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return round(float(value), 2)
    try:
        return round(float(str(value)), 2)
    except ValueError:
        return None


def _rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)
