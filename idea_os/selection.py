"""Adaptive weekly idea selection engine."""

from __future__ import annotations

from collections import defaultdict, deque
from datetime import date
import math
import random
import re
from pathlib import Path
from typing import Any

from idea_os.clustering_engine import infer_theme
from idea_os.config import load_config, planning_repo_path
from idea_os.models import MATURITY_FIELDS
from idea_os.planning import iso_week_folder
from idea_os.similarity import idea_similarity, shared_tags
from idea_os.store import REPO_ROOT, load_idea


VALUE_SCORE = {
    "low": 1.0,
    "medium": 2.0,
    "high": 3.0,
}

SOURCE_FOLDERS = ["ideas/structured", "ideas/evolving"]
WEEK_RE = re.compile(r"^(\d{4})-W(\d{2})$")


def eligible_idea_files(root: str | Path | None = None) -> list[Path]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    paths: list[Path] = []
    for folder in SOURCE_FOLDERS:
        paths.extend(sorted((repo / folder).glob("*.yaml")))
    return paths


def load_eligible_ideas(root: str | Path | None = None) -> list[dict[str, Any]]:
    return [load_idea(path) for path in eligible_idea_files(root)]


def value_to_number(value: Any) -> float:
    return VALUE_SCORE.get(str(value).strip().lower(), 0.0)


def maturity_ratio(idea: dict[str, Any]) -> float:
    maturity = idea.get("maturity", {})
    total = sum(_to_float(maturity.get(field)) for field in MATURITY_FIELDS)
    return _round(max(0.0, min(1.0, total / 20.0)))


def execution_cost(idea: dict[str, Any]) -> float:
    steps = idea.get("next_steps", [])
    step_count = len(steps) if isinstance(steps, list) else 1
    cost = min(1.0, step_count / 5.0)
    data_required = idea.get("data_required", False)
    if data_required:
        if isinstance(data_required, list):
            cost += 0.2 if data_required else 0.0
        else:
            cost += 0.2
    return _round(min(1.0, cost))


def alignment_score(idea: dict[str, Any], priority_tags: list[str]) -> float:
    if not priority_tags:
        return 0.0
    idea_tags = {str(tag) for tag in idea.get("tags", [])}
    priorities = {str(tag) for tag in priority_tags}
    return _round(len(idea_tags & priorities) / len(priorities))


def novelty_scores(ideas: list[dict[str, Any]]) -> dict[str, float]:
    scores: dict[str, float] = {}
    for idea in ideas:
        others = [other for other in ideas if other["id"] != idea["id"]]
        max_similarity = max((idea_similarity(idea, other) for other in others), default=0.0)
        scores[idea["id"]] = _round(1.0 - max_similarity)
    return scores


def compute_metrics(
    idea: dict[str, Any], ideas: list[dict[str, Any]], priority_tags: list[str]
) -> dict[str, Any]:
    novelty = novelty_scores(ideas).get(idea["id"], 1.0)
    value = idea.get("value", {})
    impact = value_to_number(value.get("impact"))
    feasibility = value_to_number(value.get("feasibility"))
    maturity = maturity_ratio(idea)
    cost = execution_cost(idea)
    alignment = alignment_score(idea, priority_tags)
    selection_score = (
        0.3 * impact
        + 0.2 * feasibility
        + 0.2 * maturity
        + 0.1 * novelty
        + 0.1 * (1.0 - cost)
        + 0.1 * alignment
    )
    return {
        "impact": impact,
        "feasibility": feasibility,
        "maturity": maturity,
        "connections": len(idea.get("connections", [])),
        "novelty": _round(novelty),
        "execution_cost": _round(cost),
        "alignment": _round(alignment),
        "selection_score": _round(selection_score),
    }


def metrics_for_ideas(ideas: list[dict[str, Any]], priority_tags: list[str]) -> dict[str, dict[str, Any]]:
    novelty = novelty_scores(ideas)
    metrics: dict[str, dict[str, Any]] = {}
    for idea in ideas:
        metric = compute_metrics(idea, ideas, priority_tags)
        metric["novelty"] = novelty.get(idea["id"], metric["novelty"])
        value = idea.get("value", {})
        impact = metric["impact"]
        feasibility = metric["feasibility"]
        metric["selection_score"] = _round(
            0.3 * impact
            + 0.2 * feasibility
            + 0.2 * metric["maturity"]
            + 0.1 * metric["novelty"]
            + 0.1 * (1.0 - metric["execution_cost"])
            + 0.1 * metric["alignment"]
        )
        metrics[idea["id"]] = metric
    return metrics


def adaptive_epsilon(
    root: str | Path | None = None,
    week: str | None = None,
    config: dict[str, Any] | None = None,
) -> tuple[float, str]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    config = config or load_config(repo)
    base = float(config.get("base_epsilon", 0.3))
    minimum = float(config.get("min_epsilon", 0.1))
    maximum = float(config.get("max_epsilon", 0.4))
    target_week = week or iso_week_folder(date.today())
    previous = previous_week_id(target_week)
    planning = planning_repo_path(repo)
    review_path = planning / "weeks" / previous / "weekly-review.md"

    if review_path.exists():
        review = parse_weekly_review(review_path.read_text(encoding="utf-8"))
        if not review["usable"]:
            return maximum, f"{previous} review metrics incomplete; exploration increased for stagnation"
        return _epsilon_from_review(review, base, minimum, maximum, previous)

    latest = latest_usable_review(planning)
    if latest is None:
        return base, "no usable weekly review found; using base epsilon"
    latest_week, review = latest
    return _epsilon_from_review(review, base, minimum, maximum, latest_week)


def parse_weekly_review(text: str) -> dict[str, Any]:
    completion = _metric(text, "Average completion rate")
    shutdown = _metric(text, "Shutdown completion rate")
    diagnosis = _text_after_label(text, "Was the week overloaded, underloaded, or about right?")
    blocker = _text_after_label(text, "Dominant blocker")
    usable = completion is not None and shutdown is not None
    return {
        "usable": usable,
        "completion": completion,
        "shutdown": shutdown,
        "diagnosis": diagnosis,
        "blocker": blocker,
    }


def latest_usable_review(planning: Path) -> tuple[str, dict[str, Any]] | None:
    reviews: list[tuple[str, dict[str, Any]]] = []
    for path in sorted(planning.glob("weeks/*/weekly-review.md")):
        week_id = path.parent.name
        review = parse_weekly_review(path.read_text(encoding="utf-8"))
        if review["usable"]:
            reviews.append((week_id, review))
    return reviews[-1] if reviews else None


def build_pools(ideas: list[dict[str, Any]], metrics: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
    if not ideas:
        return {"exploitation_pool": [], "novelty_pool": [], "random_pool": []}
    pool_size = max(1, math.ceil(len(ideas) * 0.3))
    by_score = sorted(
        ideas,
        key=lambda idea: (-metrics[idea["id"]]["selection_score"], idea["id"]),
    )
    by_novelty = sorted(
        ideas,
        key=lambda idea: (-metrics[idea["id"]]["novelty"], idea["id"]),
    )
    exploitation = [idea["id"] for idea in by_score[:pool_size]]
    novelty = [idea["id"] for idea in by_novelty[:pool_size]]
    used = set(exploitation) | set(novelty)
    random_pool = [idea["id"] for idea in by_score if idea["id"] not in used]
    return {
        "exploitation_pool": exploitation,
        "novelty_pool": novelty,
        "random_pool": random_pool,
    }


def selection_counts(total: int, epsilon: float) -> dict[str, int]:
    if total <= 0:
        return {"exploit": 0, "explore": 0, "random": 0}
    raw = {
        "exploit": total * (1.0 - epsilon),
        "explore": total * epsilon * (2.0 / 3.0),
        "random": total * epsilon * (1.0 / 3.0),
    }
    counts = {key: int(math.floor(value)) for key, value in raw.items()}
    remaining = total - sum(counts.values())
    priority = {"random": 0, "exploit": 1, "explore": 2}
    order = sorted(raw, key=lambda key: (-(raw[key] - counts[key]), priority[key]))
    for key in order[:remaining]:
        counts[key] += 1
    return counts


def select_ideas(
    ideas: list[dict[str, Any]],
    metrics: dict[str, dict[str, Any]],
    pools: dict[str, list[str]],
    epsilon: float,
    total: int,
    seed: str,
) -> list[dict[str, Any]]:
    by_id = {idea["id"]: idea for idea in ideas}
    counts = selection_counts(min(total, 10, len(ideas)), epsilon)
    selected: list[dict[str, Any]] = []
    selected_ids: set[str] = set()
    rng = random.Random(seed)

    specs = [
        ("exploit", pools["exploitation_pool"], lambda idea_id: -metrics[idea_id]["selection_score"]),
        ("explore", pools["novelty_pool"], lambda idea_id: -metrics[idea_id]["novelty"]),
        ("random", pools["random_pool"], None),
    ]
    for selection_type, pool, key_func in specs:
        candidates = [idea_id for idea_id in pool if idea_id not in selected_ids]
        if key_func is None:
            rng.shuffle(candidates)
        else:
            candidates.sort(key=lambda idea_id: (key_func(idea_id), idea_id))
        for idea_id in candidates[: counts[selection_type]]:
            selected.append(_selection_entry(by_id[idea_id], metrics[idea_id], selection_type, False))
            selected_ids.add(idea_id)

    if len(selected) < min(total, len(ideas)):
        fallback = sorted(
            [idea for idea in ideas if idea["id"] not in selected_ids],
            key=lambda idea: (-metrics[idea["id"]]["selection_score"], idea["id"]),
        )
        for idea in fallback[: min(total, len(ideas)) - len(selected)]:
            selected.append(_selection_entry(idea, metrics[idea["id"]], "exploit", True))
            selected_ids.add(idea["id"])
    return selected[: min(total, len(ideas))]


def detect_selected_clusters(
    selected: list[dict[str, Any]],
    ideas: list[dict[str, Any]],
    threshold: float,
) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    selected_ids = {entry["id"] for entry in selected}
    selected_ideas = [idea for idea in ideas if idea["id"] in selected_ids]
    adjacency: dict[str, set[str]] = defaultdict(set)
    for index, left in enumerate(selected_ideas):
        for right in selected_ideas[index + 1 :]:
            if shared_tags(left, right) or idea_similarity(left, right) > threshold:
                adjacency[left["id"]].add(right["id"])
                adjacency[right["id"]].add(left["id"])

    seen: set[str] = set()
    clusters: dict[str, dict[str, Any]] = {}
    idea_to_cluster: dict[str, str] = {}
    cluster_index = 1
    by_id = {idea["id"]: idea for idea in selected_ideas}
    for idea in sorted(selected_ideas, key=lambda item: item["id"]):
        if idea["id"] in seen:
            continue
        queue = deque([idea["id"]])
        seen.add(idea["id"])
        component: list[str] = []
        while queue:
            current = queue.popleft()
            component.append(current)
            for neighbor in sorted(adjacency[current]):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        if len(component) < 2:
            continue
        cluster_id = f"selected_cluster_{cluster_index:03d}"
        cluster_index += 1
        component_ideas = [by_id[idea_id] for idea_id in sorted(component)]
        clusters[cluster_id] = {
            "theme": infer_theme(component_ideas),
            "ideas": sorted(component),
            "research_candidate": True,
        }
        for idea_id in component:
            idea_to_cluster[idea_id] = cluster_id
    return clusters, idea_to_cluster


def distribute_across_week(selected: list[dict[str, Any]], week: str) -> dict[str, list[str]]:
    monday = monday_for_week(week)
    distribution = {
        (monday.fromordinal(monday.toordinal() + offset)).isoformat(): []
        for offset in range(5)
    }
    days = list(distribution)
    for index, entry in enumerate(selected[:10]):
        day = days[index % 5] if index < 5 else days[index - 5]
        distribution[day].append(entry["id"])
    return distribution


def build_weekly_selection(
    root: str | Path | None = None,
    week: str | None = None,
    top_n: int | None = None,
) -> dict[str, Any]:
    repo = Path(root).resolve() if root is not None else REPO_ROOT
    config = load_config(repo)
    target_week = week or iso_week_folder(date.today())
    limit = int(top_n or config.get("top_n", 5))
    priority_tags = [str(tag) for tag in config.get("priority_tags", [])]
    ideas = load_eligible_ideas(repo)
    metrics = metrics_for_ideas(ideas, priority_tags)
    epsilon, adaptive_reason = adaptive_epsilon(repo, target_week, config)
    pools = build_pools(ideas, metrics)
    seed = _selection_seed(config.get("selection_seed", "iso_week"), target_week)
    selected = select_ideas(ideas, metrics, pools, epsilon, limit, seed)
    threshold = float(config.get("similarity_threshold", 0.75))
    clusters, idea_to_cluster = detect_selected_clusters(selected, ideas, threshold)
    for entry in selected:
        cluster_id = idea_to_cluster.get(entry["id"])
        entry["cluster_id"] = cluster_id or ""
        entry["research_candidate"] = bool(cluster_id)
    distribution = distribute_across_week(selected, target_week)
    return {
        "week": target_week,
        "epsilon": _round(epsilon),
        "adaptive_reason": adaptive_reason,
        "pool_weights": {
            "exploit": _round(1.0 - epsilon),
            "explore": _round(epsilon * (2.0 / 3.0)),
            "random": _round(epsilon * (1.0 / 3.0)),
        },
        "selection_counts": selection_counts(min(limit, len(ideas)), epsilon),
        "source_folders": SOURCE_FOLDERS,
        "priority_tags": priority_tags,
        "pools": pools,
        "selected": selected,
        "clusters": clusters,
        "daily_distribution": distribution,
    }


def monday_for_week(week: str) -> date:
    match = WEEK_RE.match(week)
    if not match:
        raise ValueError(f"Invalid ISO week: {week}")
    year = int(match.group(1))
    week_number = int(match.group(2))
    return date.fromisocalendar(year, week_number, 1)


def previous_week_id(week: str) -> str:
    monday = monday_for_week(week)
    previous_monday = monday.fromordinal(monday.toordinal() - 7)
    return iso_week_folder(previous_monday)


def _selection_entry(
    idea: dict[str, Any],
    metrics: dict[str, Any],
    selection_type: str,
    fallback: bool,
) -> dict[str, Any]:
    steps = idea.get("next_steps", [])
    next_step = steps[0] if isinstance(steps, list) and steps else ""
    path = _relative_path(idea.get("_path", ""))
    reason = f"selected from {selection_type} pool"
    if fallback:
        reason += " as backfill after requested pool was exhausted"
    return {
        "id": idea["id"],
        "title": idea.get("title", ""),
        "status": idea.get("status", ""),
        "maturity_score": idea.get("score", 0),
        "selection_type": selection_type,
        "selection_score": metrics["selection_score"],
        "novelty": metrics["novelty"],
        "metrics": metrics,
        "path": path,
        "next_step": next_step,
        "experiment": f"Run a bounded test for {idea.get('title', '')}: {next_step}",
        "measurable_output": "One recorded result that can update insight, maturity, or status.",
        "reason": reason,
    }


def _relative_path(path_text: str) -> str:
    if not path_text:
        return ""
    path = Path(path_text).resolve()
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _epsilon_from_review(
    review: dict[str, Any],
    base: float,
    minimum: float,
    maximum: float,
    week: str,
) -> tuple[float, str]:
    completion = float(review.get("completion") or 0.0)
    shutdown = float(review.get("shutdown") or 0.0)
    diagnosis = str(review.get("diagnosis", "")).lower()
    blocker = str(review.get("blocker", "")).lower()
    if completion >= 0.85 and shutdown >= 0.80 and "overloaded" not in diagnosis:
        return minimum, f"{week} success high; exploration reduced"
    if completion < 0.70 or "overloaded" in diagnosis or blocker in {"fatigue", "overscope", "avoidance"}:
        return maximum, f"{week} stagnation or overload detected; exploration increased"
    return base, f"{week} review within normal range; using base epsilon"


def _selection_seed(configured: Any, week: str) -> str:
    if str(configured) == "iso_week":
        return week
    return str(configured)


def _metric(text: str, label: str) -> float | None:
    for line in text.splitlines():
        if line.strip().startswith(f"- {label}:"):
            value = line.split(":", 1)[1].strip()
            if not value:
                return None
            match = re.search(r"-?\d+(?:\.\d+)?", value)
            return float(match.group(0)) if match else None
    return None


def _text_after_label(text: str, label: str) -> str:
    for line in text.splitlines():
        if line.strip().startswith(f"- {label}:"):
            return line.split(":", 1)[1].strip()
    return ""


def _to_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _round(value: float) -> float:
    return round(value, 4)
