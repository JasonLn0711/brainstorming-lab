"""Generate research candidates and briefs from mature clusters."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from idea_os.models import maturity_value, parse_score, total_maturity


def generate_research_candidates(
    clusters: dict[str, dict[str, Any]],
    ideas: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    by_id = {idea["id"]: idea for idea in ideas}
    eligible: list[tuple[str, dict[str, Any], list[dict[str, Any]]]] = []
    for cluster_id, cluster in clusters.items():
        cluster_ideas = [by_id[idea_id] for idea_id in cluster.get("ideas", []) if idea_id in by_id]
        if _cluster_is_research_ready(cluster, cluster_ideas):
            eligible.append((cluster_id, cluster, cluster_ideas))

    eligible.sort(key=lambda item: (-parse_score(item[1].get("cluster_score"), 100), item[0]))
    candidates: dict[str, dict[str, Any]] = {}
    for index, (cluster_id, cluster, cluster_ideas) in enumerate(eligible, start=1):
        candidate_id = f"research_candidate_{index:04d}"
        research_score = _research_readiness_score(cluster, cluster_ideas)
        title = _candidate_title(cluster, cluster_ideas)
        candidates[candidate_id] = {
            "candidate_id": candidate_id,
            "title": title,
            "source_cluster": cluster_id,
            "source_ideas": [idea["id"] for idea in cluster_ideas],
            "normalized_problem": cluster.get("normalized_problem", ""),
            "research_question": _research_question(cluster, cluster_ideas),
            "why_now": _why_now(cluster_ideas),
            "possible_contribution": _possible_contribution(cluster_ideas),
            "baseline": _merged_list(cluster_ideas, "baseline"),
            "metrics": _merged_list(cluster_ideas, "metrics"),
            "minimum_viable_experiment": _minimum_viable_experiment(cluster_ideas),
            "risks": _risks(cluster_ideas),
            "next_steps": _merged_list(cluster_ideas, "next_steps")[:5],
            "research_score": f"{research_score}/100",
            "research_level": research_level(research_score),
        }
    return candidates


def render_research_brief(candidate: dict[str, Any]) -> str:
    lines = [
        f"# {candidate.get('title', candidate.get('candidate_id', 'Research Candidate'))}",
        "",
        "## Normalized Problem Statement",
        "",
        str(candidate.get("normalized_problem", "")),
        "",
        "## Research Question",
        "",
        str(candidate.get("research_question", "")),
        "",
        "## Source Ideas",
        "",
    ]
    lines.extend(f"- `{idea_id}`" for idea_id in candidate.get("source_ideas", []))
    lines.extend(["", "## Why This Matters", "", str(candidate.get("why_now", "")), ""])
    lines.extend(["## Hypothesis", "", _hypothesis(candidate), ""])
    lines.extend(["## Baseline", ""])
    lines.extend(_list_lines(candidate.get("baseline", [])))
    lines.extend(["", "## Metrics", ""])
    lines.extend(_list_lines(candidate.get("metrics", [])))
    lines.extend(["", "## Minimum Viable Experiment", "", str(candidate.get("minimum_viable_experiment", "")), ""])
    lines.extend(["## Risks", ""])
    lines.extend(_list_lines(candidate.get("risks", [])))
    lines.extend(["", "## Next Steps", ""])
    lines.extend(_list_lines(candidate.get("next_steps", [])))
    lines.extend(["", "## Readiness Score", "", f"Research Readiness: {candidate.get('research_score', '0/100')}"])
    return "\n".join(lines).rstrip() + "\n"


def write_research_briefs(
    candidates: dict[str, dict[str, Any]],
    root: str | Path,
) -> list[Path]:
    output_dir = Path(root).resolve() / "research" / "research_briefs"
    output_dir.mkdir(parents=True, exist_ok=True)
    expected = {f"{candidate_id}.md" for candidate_id in candidates}
    for old_path in output_dir.glob("*.md"):
        if old_path.name not in expected:
            old_path.unlink()
    paths: list[Path] = []
    for candidate_id, candidate in candidates.items():
        path = output_dir / f"{candidate_id}.md"
        path.write_text(render_research_brief(candidate), encoding="utf-8")
        paths.append(path)
    return paths


def research_level(score: int) -> str:
    if score <= 49:
        return "topic_only"
    if score <= 64:
        return "discussable"
    if score <= 79:
        return "small_experiment_ready"
    if score <= 89:
        return "proposal_ready"
    return "independent_repo_or_paper_ready"


def _cluster_is_research_ready(cluster: dict[str, Any], ideas: list[dict[str, Any]]) -> bool:
    if len(ideas) < 2:
        return False
    return (
        _avg(ideas, total_maturity) >= 65
        and _avg(ideas, lambda idea: maturity_value(idea, "testability")) >= 10
        and _avg(ideas, lambda idea: maturity_value(idea, "evidence_support")) >= 8
        and _avg(ideas, lambda idea: maturity_value(idea, "feasibility")) >= 8
        and bool(cluster.get("normalized_problem"))
        and all(_has_items(idea.get("baseline", [])) for idea in ideas)
        and all(_has_items(idea.get("metrics", [])) for idea in ideas)
    )


def _research_readiness_score(cluster: dict[str, Any], ideas: list[dict[str, Any]]) -> int:
    importance = 20 if any("need" in _text(idea).lower() or "workflow" in _text(idea).lower() for idea in ideas) else 12
    testability = min(20, round(_avg(ideas, lambda idea: maturity_value(idea, "testability")) * 20 / 15))
    evidence = min(15, round(_avg(ideas, lambda idea: maturity_value(idea, "evidence_support"))))
    feasibility = min(15, round(_avg(ideas, lambda idea: maturity_value(idea, "feasibility"))))
    novelty = min(15, round(_avg(ideas, lambda idea: maturity_value(idea, "novelty")) * 15 / 10))
    execution = 15 if all(_has_items(idea.get("next_steps", [])) for idea in ideas) else 8
    return min(100, importance + testability + evidence + feasibility + novelty + execution)


def _candidate_title(cluster: dict[str, Any], ideas: list[dict[str, Any]]) -> str:
    theme = str(cluster.get("theme", "")).strip()
    if theme:
        return f"Research candidate: {theme}"
    return f"Research candidate: {ideas[0].get('title', 'untitled')}"


def _research_question(cluster: dict[str, Any], ideas: list[dict[str, Any]]) -> str:
    problem = str(cluster.get("normalized_problem", "")).rstrip(".")
    metrics = ", ".join(_merged_list(ideas, "metrics")[:3]) or "defined outcome metrics"
    return f"Can a bounded method for this problem improve {metrics} compared with the baseline?"


def _why_now(ideas: list[dict[str, Any]]) -> str:
    tags = sorted({str(tag) for idea in ideas for tag in idea.get("tags", [])})
    return "The cluster has multiple connected idea nodes, shared evidence, and measurable next steps" + (
        f" across {', '.join(tags[:4])}." if tags else "."
    )


def _possible_contribution(ideas: list[dict[str, Any]]) -> str:
    return "A reusable evaluation frame that compares baseline workflow performance against a small, auditable intervention."


def _minimum_viable_experiment(ideas: list[dict[str, Any]]) -> str:
    steps = _merged_list(ideas, "next_steps")
    return steps[0] if steps else "Create a small fixture, run the baseline, run the proposed method, and compare metrics."


def _risks(ideas: list[dict[str, Any]]) -> list[str]:
    text = " ".join(_text(idea).lower() for idea in ideas)
    risks = []
    if "clinical" in text or "patient" in text:
        risks.append("Clinical safety and privacy boundaries must stay explicit.")
    if "review" in text or "candidate" in text:
        risks.append("Reviewer burden may move rather than shrink if candidate quality is weak.")
    if "automation" in text or "openclaw" in text:
        risks.append("Automation must preserve approval gates and rollback.")
    return risks or ["The cluster may be too broad unless the first experiment stays small."]


def _merged_list(ideas: list[dict[str, Any]], field: str) -> list[str]:
    values: list[str] = []
    for idea in ideas:
        for value in idea.get(field, []) or []:
            text = _value_text(value)
            if text and text not in values:
                values.append(text)
    return values


def _list_lines(values: Any) -> list[str]:
    if not isinstance(values, list) or not values:
        return ["- Not defined."]
    return [f"- {str(value)}" for value in values]


def _hypothesis(candidate: dict[str, Any]) -> str:
    metric = ", ".join(candidate.get("metrics", [])[:2]) or "the target metric"
    return f"If the cluster's shared problem framing is correct, the minimum viable experiment should improve {metric} over the baseline."


def _avg(ideas: list[dict[str, Any]], getter) -> float:
    if not ideas:
        return 0.0
    return sum(float(getter(idea)) for idea in ideas) / len(ideas)


def _has_items(value: Any) -> bool:
    return isinstance(value, list) and any(str(item).strip() for item in value)


def _text(idea: dict[str, Any]) -> str:
    return " ".join(str(idea.get(field, "")) for field in ["title", "summary"])


def _value_text(value: Any) -> str:
    if isinstance(value, dict):
        if "name" in value:
            return str(value["name"])
        return " ".join(str(part) for part in value.values() if str(part).strip())
    return str(value)
