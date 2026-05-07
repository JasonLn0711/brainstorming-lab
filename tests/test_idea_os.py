from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from idea_os.clustering_engine import build_clusters
from idea_os.graphing import build_graph
from idea_os.indexer import generate_indexes
from idea_os.merge import detect_merge_candidates, merge_decision
from idea_os.models import classify_score, score_idea, validate_idea
from idea_os.paper_lab import EXPECTED_MARKDOWN_FILES, validate_paper_lab
from idea_os.paper_shortlist import validate_shortlists
from idea_os.planning import insert_or_replace_block, render_today_block
from idea_os.problem import normalize_idea_problem
from idea_os.research_engine import generate_research_candidates
from idea_os.selection import (
    adaptive_epsilon,
    build_pools,
    build_weekly_selection,
    compute_metrics,
    metrics_for_ideas,
    novelty_scores,
    selection_counts,
    value_to_number,
)
from idea_os.store import make_template_idea, next_idea_id, path_for_idea, save_idea
from idea_os.yaml_io import load_yaml, save_yaml


REPO = Path(__file__).resolve().parents[1]


class IdeaOSTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "brainstorming-lab"
        for folder in [
            "ideas/raw",
            "ideas/evolving",
            "ideas/structured",
            "ideas/executing",
            "ideas/archived",
            "config",
            "index",
            "research",
            "clusters",
            "clustering",
            "graph",
        ]:
            (self.root / folder).mkdir(parents=True, exist_ok=True)
        save_yaml(
            self.root / "config" / "settings.yaml",
            {
                "planning_repo_path": "../planning-everything-track",
                "top_n": 5,
                "similarity_threshold": 0.5,
                "priority_tags": ["workflow", "ai-triage"],
                "base_epsilon": 0.3,
                "min_epsilon": 0.1,
                "max_epsilon": 0.4,
                "selection_seed": "iso_week",
            },
        )
        self.planning = Path(self.tmp.name) / "planning-everything-track"
        (self.planning / "weeks" / "2026-W18").mkdir(parents=True, exist_ok=True)
        (self.planning / "weeks" / "2026-W18" / "weekly-review.md").write_text(
            "# Weekly review\n\n## Metrics snapshot\n- Average completion rate:\n- Shutdown completion rate:\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_yaml_round_trip(self) -> None:
        data = {
            "id": "idea_000001",
            "tags": ["ai", "triage"],
            "maturity": {"clarity": 4, "testability": 3},
            "summary": "Line one\nLine two",
        }
        path = self.root / "ideas" / "raw" / "round_trip.yaml"
        save_yaml(path, data)
        self.assertEqual(load_yaml(path), data)

    def test_yaml_reader_accepts_pyyaml_style_files(self) -> None:
        path = self.root / "ideas" / "structured" / "pyyaml_style.yaml"
        path.write_text(
            """id: idea_000001
title: Legacy PyYAML style
tags:
- ai
- triage
summary: Given a long line, preserve wrapped
  scalar continuation when reading.
variants:
- name: Reply-only
  definition: Inspect replies.
- name: Reply plus cue
  definition: Inspect replies with a
    continuation line.
empty_mapping: {}
""",
            encoding="utf-8",
        )
        loaded = load_yaml(path)
        self.assertEqual(loaded["tags"], ["ai", "triage"])
        self.assertEqual(
            loaded["summary"],
            "Given a long line, preserve wrapped scalar continuation when reading.",
        )
        self.assertEqual(loaded["variants"][1]["definition"], "Inspect replies with a continuation line.")
        self.assertEqual(loaded["empty_mapping"], {})

    def test_score_classification_and_validation(self) -> None:
        idea = make_template_idea("idea_000001", "Scoring test")
        idea["baseline"] = ["manual workflow baseline"]
        idea["metrics"] = ["time to decision", "review burden"]
        idea["evidence"] = ["observation", "concrete case", "real-world workflow need"]
        idea["next_steps"] = ["Run a bounded fixture experiment."]
        score_idea(idea)
        self.assertRegex(idea["maturity_score"], r"^\d+/100$")
        self.assertNotIn("score", idea)
        self.assertEqual(classify_score(74), "research_candidate")
        self.assertEqual(validate_idea(idea), [])

    def test_id_generation_and_bidirectional_link_script(self) -> None:
        left = make_template_idea("idea_000001", "Left idea", tags=["workflow"])
        right = make_template_idea("idea_000002", "Right idea", tags=["workflow"])
        save_idea(path_for_idea(left, self.root), left)
        save_idea(path_for_idea(right, self.root), right)
        self.assertEqual(next_idea_id(self.root), "idea_000003")

        subprocess.run(
            [
                sys.executable,
                str(REPO / "scripts" / "link_ideas.py"),
                "idea_000001",
                "idea_000002",
                "--root",
                str(self.root),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        updated_left = load_yaml(path_for_idea(left, self.root))
        updated_right = load_yaml(path_for_idea(right, self.root))
        self.assertIn("idea_000002", updated_left["connections"])
        self.assertIn("idea_000001", updated_right["connections"])
        self.assertTrue(list((self.root / "backups" / "idea_yaml").glob("**/*.yaml")))

    def test_problem_normalization_and_merge_detection(self) -> None:
        idea = make_template_idea("idea_000001", "AI triage", tags=["healthcare"])
        idea["problem_statement"] = "AI triage"
        idea["summary"] = ""
        normalize_idea_problem(idea)
        self.assertEqual(idea["normalization_status"], "needs_review")
        self.assertIn("Given", idea["problem_statement"]["normalized"])
        self.assertEqual(merge_decision(82), "strong_cluster_or_synthesis")

        left = self._idea("idea_000001", "AI triage", 80, ["ai-triage"], ["idea_000002"])
        right = self._idea("idea_000002", "Clinical review triage", 80, ["ai-triage"], ["idea_000001"])
        candidates = detect_merge_candidates([left, right], minimum_score=60)
        self.assertTrue(candidates)

    def test_graph_cluster_and_research_candidate(self) -> None:
        ideas = [
            self._idea("idea_000001", "AI triage", 13, ["ai-triage"], ["idea_000002"]),
            self._idea("idea_000002", "Review triage", 15, ["ai-triage"], ["idea_000001"]),
            self._idea("idea_000003", "Loose note", 4, ["misc"], []),
        ]
        graph = build_graph(ideas, threshold=0.5)
        self.assertTrue(any("manual_connection" in edge["reasons"] for edge in graph["edges"]))

        clusters = build_clusters(ideas, threshold=60)
        self.assertIn("cluster_0001", clusters)
        self.assertGreaterEqual(len(clusters["cluster_0001"]["ideas"]), 2)

        candidates = generate_research_candidates(clusters, ideas)
        self.assertIn("research_candidate_0001", candidates)

    def test_index_generation(self) -> None:
        idea = self._idea("idea_000001", "Indexed idea", 12, ["index"], [])
        path = path_for_idea(idea, self.root)
        save_idea(path, idea)
        loaded = dict(idea)
        loaded["_path"] = str(path)
        idea_index, tag_index, cluster_index, research_index = generate_indexes([loaded], self.root)
        self.assertIn("Indexed idea", idea_index.read_text(encoding="utf-8"))
        self.assertIn("/100", idea_index.read_text(encoding="utf-8"))
        self.assertIn("index", tag_index.read_text(encoding="utf-8"))
        self.assertTrue(cluster_index.exists())
        self.assertTrue(research_index.exists())

    def test_planning_marker_idempotency(self) -> None:
        selection = {
            "selected": [
                {
                    "id": "idea_000001",
                    "title": "Planning bridge",
                    "selection_type": "exploit",
                    "selection_score": 1.5,
                    "maturity_score": "74/100",
                    "novelty": 0.3,
                    "experiment": "Run a tiny test.",
                    "measurable_output": "One note.",
                    "path": "ideas/structured/idea_000001_planning_bridge.yaml",
                }
            ]
        }
        first = insert_or_replace_block("# Daily note\n", render_today_block(selection))
        second = insert_or_replace_block(first, render_today_block(selection))
        self.assertEqual(first, second)
        self.assertEqual(second.count("<!-- IDEA_OS_TODAY_START -->"), 1)
        self.assertIn("brainstorming-lab/ideas/structured/idea_000001_planning_bridge.yaml", second)

    def test_selection_metrics_and_novelty(self) -> None:
        ideas = [
            self._idea("idea_000001", "Workflow AI", 12, ["workflow", "ai-triage"], []),
            self._idea("idea_000002", "Different hardware", 8, ["hardware"], []),
        ]
        metric = compute_metrics(ideas[0], ideas, ["workflow", "ai-triage"])
        self.assertEqual(value_to_number("high"), 3.0)
        self.assertEqual(metric["impact"], 2.0)
        self.assertEqual(metric["alignment"], 1.0)
        self.assertIn("selection_score", metric)
        novelty = novelty_scores(ideas)
        self.assertGreaterEqual(novelty["idea_000002"], novelty["idea_000001"])

    def test_adaptive_epsilon_and_deterministic_selection(self) -> None:
        ideas = [
            self._idea("idea_000001", "Workflow AI", 13, ["workflow", "ai-triage"], ["idea_000002"]),
            self._idea("idea_000002", "Triage review", 15, ["ai-triage"], ["idea_000001"]),
            self._idea("idea_000003", "Novel hardware", 10, ["hardware"], []),
            self._idea("idea_000004", "Workflow bridge", 12, ["workflow"], []),
            self._idea("idea_000005", "Research routing", 11, ["research"], []),
        ]
        for idea in ideas:
            save_idea(path_for_idea(idea, self.root), idea)

        epsilon, reason = adaptive_epsilon(self.root, "2026-W19")
        self.assertEqual(epsilon, 0.4)
        self.assertIn("incomplete", reason)

        selection = build_weekly_selection(self.root, "2026-W19", 5)
        self.assertEqual(selection["selection_counts"], {"exploit": 3, "explore": 1, "random": 1})
        self.assertEqual(len(selection["selected"]), 5)
        self.assertEqual(selection, build_weekly_selection(self.root, "2026-W19", 5))
        self.assertTrue(any(item["selection_type"] == "random" for item in selection["selected"]))

    def test_pool_construction_cluster_detection_and_distribution(self) -> None:
        ideas = [
            self._idea("idea_000001", "AI triage", 13, ["ai-triage"], ["idea_000002"]),
            self._idea("idea_000002", "Review triage", 15, ["ai-triage"], ["idea_000001"]),
            self._idea("idea_000003", "Workflow bridge", 12, ["workflow"], []),
        ]
        for idea in ideas:
            save_idea(path_for_idea(idea, self.root), idea)
        loaded = [dict(idea, _path=str(path_for_idea(idea, self.root))) for idea in ideas]
        metrics = metrics_for_ideas(loaded, ["ai-triage"])
        pools = build_pools(loaded, metrics)
        self.assertTrue(pools["exploitation_pool"])
        self.assertEqual(selection_counts(5, 0.3), {"exploit": 3, "explore": 1, "random": 1})
        selection = build_weekly_selection(self.root, "2026-W19", 3)
        self.assertTrue(selection["clusters"])
        for ideas_for_day in selection["daily_distribution"].values():
            self.assertLessEqual(len(ideas_for_day), 2)

    def test_week_feedback_pull_updates_yaml(self) -> None:
        idea = self._idea("idea_000001", "Feedback idea", 12, ["workflow"], [])
        path = path_for_idea(idea, self.root)
        save_idea(path, idea)
        day_dir = self.planning / "weeks" / "2026-W19" / "days"
        day_dir.mkdir(parents=True, exist_ok=True)
        (day_dir / "2026-05-04.md").write_text(
            """# Daily note

<!-- IDEA_OS_FEEDBACK_START -->
idea_000001:
  insight: "The experiment changed the next test."
  experiment_result: "Useful signal"
<!-- IDEA_OS_FEEDBACK_END -->
""",
            encoding="utf-8",
        )
        dry_run = subprocess.run(
            [
                sys.executable,
                str(REPO / "scripts" / "pull_feedback.py"),
                "--week",
                "2026-W19",
                "--dry-run",
                "--root",
                str(self.root),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("idea_000001", dry_run.stdout)
        self.assertNotIn("The experiment changed the next test.", load_yaml(path)["insights"])
        subprocess.run(
            [
                sys.executable,
                str(REPO / "scripts" / "pull_feedback.py"),
                "--week",
                "2026-W19",
                "--root",
                str(self.root),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        updated = load_yaml(path)
        self.assertIn("The experiment changed the next test.", updated["insights"])
        self.assertIn("Experiment result: Useful signal", updated["insights"])
        self.assertIn("maturity_score", updated)

    def test_weekly_paper_lab_validation(self) -> None:
        paper_dir = self.root / "weekly-paper-lab" / "papers" / "2026-W19-agent-memory"
        paper_dir.mkdir(parents=True, exist_ok=True)
        save_yaml(paper_dir / "paper.yaml", self._paper_record())
        self._write_expected_paper_markdown(paper_dir)

        self.assertEqual(validate_paper_lab(self.root), [])

        (paper_dir / "07_scoring_report.md").unlink()
        errors = validate_paper_lab(self.root)
        self.assertTrue(any("missing 07_scoring_report.md" in error for error in errors))
        self._write_expected_paper_markdown(paper_dir)

        (paper_dir / "06_research_idea_seed.md").unlink()
        errors = validate_paper_lab(self.root)
        self.assertTrue(any("missing 06_research_idea_seed.md" in error for error in errors))

    def test_weekly_paper_lab_requires_recomputed_connections_and_synthesis(self) -> None:
        paper_dir = self.root / "weekly-paper-lab" / "papers" / "2026-W19-agent-memory"
        paper_dir.mkdir(parents=True, exist_ok=True)
        bad = self._paper_record()
        bad["idea_connections"][0]["connection_strength"]["score"] = 99
        bad["synthesis_assessment"]["synthesis_score"] = 19
        save_yaml(paper_dir / "paper.yaml", bad)
        self._write_expected_paper_markdown(paper_dir)

        errors = validate_paper_lab(self.root)
        self.assertTrue(any("connection_strength.score must be 100" in error for error in errors))
        self.assertTrue(any("synthesis_assessment.synthesis_score must be 20" in error for error in errors))

    def test_check_paper_lab_script_reports_invalid_record(self) -> None:
        paper_dir = self.root / "weekly-paper-lab" / "papers" / "2026-W19-invalid"
        paper_dir.mkdir(parents=True, exist_ok=True)
        bad = self._paper_record()
        bad["reproduction_level"] = {"level": 9}
        save_yaml(paper_dir / "paper.yaml", bad)
        self._write_expected_paper_markdown(paper_dir)

        result = subprocess.run(
            [
                sys.executable,
                str(REPO / "scripts" / "check_paper_lab.py"),
                "--root",
                str(self.root),
            ],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("reproduction_level.level", result.stdout)

    def test_weekly_paper_shortlist_validation(self) -> None:
        shortlist_dir = self.root / "weekly-paper-lab" / "shortlists"
        shortlist_dir.mkdir(parents=True, exist_ok=True)
        save_yaml(shortlist_dir / "2026-W19.yaml", self._shortlist_record())

        self.assertEqual(validate_shortlists(self.root), [])

        bad = self._shortlist_record()
        bad["candidates"][0]["candidate_score"] = 100
        save_yaml(shortlist_dir / "2026-W19.yaml", bad)
        errors = validate_shortlists(self.root)
        self.assertTrue(any("candidate_score must be 99" in error for error in errors))

    def test_weekly_paper_shortlist_rejects_previously_selected_item(self) -> None:
        paper_dir = self.root / "weekly-paper-lab" / "papers" / "2026-W19-selected-paper"
        paper_dir.mkdir(parents=True, exist_ok=True)
        selected = self._paper_record()
        selected["paper_id"] = "2026-W19-selected-paper"
        selected["week"] = "2026-W19"
        selected["title"] = "Already Selected Research Essay"
        selected["source_urls"] = ["https://example.com/already-selected"]
        save_yaml(paper_dir / "paper.yaml", selected)

        shortlist_dir = self.root / "weekly-paper-lab" / "shortlists"
        shortlist_dir.mkdir(parents=True, exist_ok=True)
        later = self._shortlist_record()
        later["week"] = "2026-W20"
        later["generated_at"] = "2026-05-14"
        later["candidates"][0]["title"] = "Fresh wrapper around old selection"
        later["candidates"][0]["evidence_sources"]["paper_url"] = "https://example.com/already-selected?utm_source=test"
        save_yaml(shortlist_dir / "2026-W20.yaml", later)

        errors = validate_shortlists(self.root)
        self.assertTrue(any("already selected before" in error for error in errors))

    def test_current_week_selected_record_does_not_block_own_shortlist(self) -> None:
        paper_dir = self.root / "weekly-paper-lab" / "papers" / "2026-W19-selected-paper"
        paper_dir.mkdir(parents=True, exist_ok=True)
        selected = self._paper_record()
        selected["paper_id"] = "paper_1"
        selected["week"] = "2026-W19"
        selected["title"] = "Candidate paper_1"
        selected["source_urls"] = ["https://example.com/paper_1"]
        save_yaml(paper_dir / "paper.yaml", selected)

        shortlist_dir = self.root / "weekly-paper-lab" / "shortlists"
        shortlist_dir.mkdir(parents=True, exist_ok=True)
        save_yaml(shortlist_dir / "2026-W19.yaml", self._shortlist_record())

        self.assertEqual(validate_shortlists(self.root), [])

    def test_weekly_paper_shortlist_rejects_duplicate_candidates(self) -> None:
        shortlist_dir = self.root / "weekly-paper-lab" / "shortlists"
        shortlist_dir.mkdir(parents=True, exist_ok=True)
        bad = self._shortlist_record()
        bad["candidates"][1]["evidence_sources"]["paper_url"] = bad["candidates"][0]["evidence_sources"]["paper_url"]
        save_yaml(shortlist_dir / "2026-W19.yaml", bad)

        errors = validate_shortlists(self.root)
        self.assertTrue(any("duplicates another candidate in this shortlist" in error for error in errors))

    def test_check_paper_shortlist_script_reports_score_mismatch(self) -> None:
        shortlist_dir = self.root / "weekly-paper-lab" / "shortlists"
        shortlist_dir.mkdir(parents=True, exist_ok=True)
        bad = self._shortlist_record()
        bad["candidates"][0]["scores"]["rtx5080_feasibility"]["score"] = 19
        save_yaml(shortlist_dir / "2026-W19.yaml", bad)

        result = subprocess.run(
            [
                sys.executable,
                str(REPO / "scripts" / "check_paper_shortlist.py"),
                "--root",
                str(self.root),
            ],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("scores.rtx5080_feasibility.score must be 20", result.stdout)

    def test_malformed_yaml_is_reported_by_cli(self) -> None:
        bad = self.root / "ideas" / "raw" / "bad.yaml"
        bad.write_text("id: bad\n  broken: true\n", encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                str(REPO / "scripts" / "normalize_problem.py"),
                "--root",
                str(self.root),
            ],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ERROR", result.stdout)

    def _idea(self, idea_id: str, title: str, maturity_hint: int, tags: list[str], connections: list[str]) -> dict:
        idea = make_template_idea(idea_id, title, tags=tags)
        idea["summary"] = f"{title} uses triage evidence routing and reviewer workflow for a concrete case with a benchmark fixture."
        idea["problem_statement"] = {
            "raw": "Given noisy inputs, optimize useful review targets under safety and audit constraints.",
            "normalized": "Given noisy review inputs, optimize review-worthy target selection under constraints of safety, auditability, and reviewer capacity.",
            "structure": {
                "given": "noisy review inputs",
                "optimize": "review-worthy target selection",
                "constraints": ["safety", "auditability", "reviewer capacity"],
            },
        }
        idea["connections"] = connections
        idea["baseline"] = ["manual review queue baseline"]
        idea["metrics"] = ["time to first useful action", "review burden", "candidate precision"]
        idea["evidence"] = ["observation", "concrete case", "benchmark reference", "real-world workflow need"]
        idea["assumptions"] = ["The useful output is safer routing, not autonomous confirmation."]
        idea["next_steps"] = ["Run a bounded synthetic fixture experiment within one week."]
        score_idea(idea)
        return idea

    def _write_expected_paper_markdown(self, paper_dir: Path) -> None:
        for filename in EXPECTED_MARKDOWN_FILES:
            if filename == "07_scoring_report.md":
                (paper_dir / filename).write_text(
                    "\n".join(
                        [
                            "# Scoring Report",
                            "",
                            "## Shortlist Triage Scoring",
                            "",
                            "Candidate score and weekly pick score are recomputed from fixed evidence fields.",
                            "",
                            "## Candidate Selection Explanation",
                            "",
                            "The selected candidate is preferred because it supports a bounded reproduction loop.",
                            "",
                            "## Idea Connection Scoring",
                            "",
                            "Connection scores are recomputed from listed overlaps, methods, metrics, and tests.",
                            "",
                            "## Synthesis Scoring",
                            "",
                            "Synthesis score is recomputed from transferable method and fixture evidence.",
                            "",
                            "## Evidence Gaps And Overrides",
                            "",
                            "Unknown evidence is not guessed and contributes zero.",
                            "",
                        ]
                    ),
                    encoding="utf-8",
                )
            else:
                (paper_dir / filename).write_text(f"# {filename}\n", encoding="utf-8")

    def _shortlist_record(self) -> dict:
        return {
            "rubric_version": "paper_lab_rubric_v1",
            "week": "2026-W19",
            "cycle_slot": "main_a",
            "generated_at": "2026-05-07",
            "candidates": [
                self._shortlist_candidate("paper_1", True, 99, 99.0),
                self._shortlist_candidate("paper_2", False, 1, 1.0),
                self._shortlist_candidate("paper_3", False, 1, 1.0),
            ],
        }

    def _shortlist_candidate(self, paper_id: str, selected: bool, candidate_score: int, pick_score: float) -> dict:
        if selected:
            scores = self._strong_shortlist_scores()
            selection_reason = "Best bounded paper for this week's reproduction and research-question loop."
            rejected_reason = ""
        else:
            scores = self._weak_shortlist_scores()
            selection_reason = ""
            rejected_reason = "Rejected because evidence does not support a bounded reproduction this week."
        return {
            "paper_id": paper_id,
            "title": f"Candidate {paper_id}",
            "selected": selected,
            "evidence_sources": {
                "paper_url": f"https://example.com/{paper_id}",
                "code_url": "",
                "dataset_url": "",
                "hf_trending_url": "",
                "openalex_url": "",
                "checked_at": "2026-05-07",
            },
            "scores": scores,
            "candidate_score": candidate_score,
            "weekly_pick_score": pick_score,
            "selection_reason": selection_reason,
            "rejected_reason": rejected_reason,
        }

    def _strong_shortlist_scores(self) -> dict:
        return {
            "recency_discussion": self._dimension(
                20,
                {
                    "published_within_30_days": True,
                    "published_within_90_days": True,
                    "hf_trending_present": True,
                    "github_stars_100_plus": True,
                    "github_stars_500_plus": True,
                    "social_discussion_present": True,
                    "benchmark_or_leaderboard_mentioned": True,
                },
            ),
            "idea_os_connection": self._dimension(
                19,
                {
                    "matches_existing_project": True,
                    "matches_existing_research_thread": True,
                    "matches_existing_idea_yaml": True,
                    "can_update_existing_method": True,
                    "only_general_interest": False,
                },
            ),
            "rtx5080_feasibility": self._dimension(
                20,
                {
                    "official_code_available": True,
                    "single_gpu_possible": True,
                    "fits_16gb_or_24gb_vram": True,
                    "small_dataset_or_fixture_possible": True,
                    "runtime_under_4_hours": True,
                    "docker_or_conda_install_clear": True,
                },
            ),
            "code_data_benchmark": self._dimension(
                20,
                {
                    "official_code": True,
                    "unofficial_code": False,
                    "dataset_available": True,
                    "benchmark_available": True,
                    "clear_metrics": True,
                    "reproducible_commands_or_demo": True,
                },
            ),
            "research_question_potential": self._dimension(
                20,
                {
                    "has_explicit_limitation_section": True,
                    "has_failure_cases": True,
                    "has_evaluation_gap": True,
                    "has_deployment_gap": True,
                    "has_theory_or_mechanism_gap": True,
                    "can_generate_3_questions": True,
                },
            ),
            "novelty_or_transfer": self._dimension(
                20,
                {
                    "not_duplicate_of_recent_lab_pick": True,
                    "introduces_new_problem_frame": True,
                    "introduces_new_method_family": True,
                    "has_transfer_path_to_other_domain": True,
                },
            ),
        }

    def _weak_shortlist_scores(self) -> dict:
        return {
            "recency_discussion": self._dimension(
                0,
                {
                    "published_within_30_days": False,
                    "published_within_90_days": False,
                    "hf_trending_present": False,
                    "github_stars_100_plus": False,
                    "github_stars_500_plus": False,
                    "social_discussion_present": False,
                    "benchmark_or_leaderboard_mentioned": False,
                },
            ),
            "idea_os_connection": self._dimension(
                1,
                {
                    "matches_existing_project": False,
                    "matches_existing_research_thread": False,
                    "matches_existing_idea_yaml": False,
                    "can_update_existing_method": False,
                    "only_general_interest": True,
                },
            ),
            "rtx5080_feasibility": self._dimension(
                0,
                {
                    "official_code_available": False,
                    "single_gpu_possible": False,
                    "fits_16gb_or_24gb_vram": False,
                    "small_dataset_or_fixture_possible": False,
                    "runtime_under_4_hours": False,
                    "docker_or_conda_install_clear": False,
                },
            ),
            "code_data_benchmark": self._dimension(
                0,
                {
                    "official_code": False,
                    "unofficial_code": False,
                    "dataset_available": False,
                    "benchmark_available": False,
                    "clear_metrics": False,
                    "reproducible_commands_or_demo": False,
                },
            ),
            "research_question_potential": self._dimension(
                0,
                {
                    "has_explicit_limitation_section": False,
                    "has_failure_cases": False,
                    "has_evaluation_gap": False,
                    "has_deployment_gap": False,
                    "has_theory_or_mechanism_gap": False,
                    "can_generate_3_questions": False,
                },
            ),
            "novelty_or_transfer": self._dimension(
                0,
                {
                    "not_duplicate_of_recent_lab_pick": False,
                    "introduces_new_problem_frame": False,
                    "introduces_new_method_family": False,
                    "has_transfer_path_to_other_domain": False,
                },
            ),
        }

    def _dimension(self, score: int, evidence: dict) -> dict:
        return {
            "score": score,
            "rule_version": "paper_lab_rubric_v1",
            "evidence": evidence,
        }

    def _paper_record(self) -> dict:
        return {
            "paper_id": "paper_2026_W19_agent_memory",
            "week": "2026-W19",
            "cycle_slot": "main_a",
            "domain_type": "ai_agent_llm_cybersecurity",
            "title": "Agent memory paper",
            "source_urls": ["https://example.com/paper"],
            "triage_score": {
                "total": 80,
                "recency_discussion": 16,
                "idea_os_connection": 16,
                "rtx5080_feasibility": 16,
                "code_data_benchmark": 16,
                "research_question_potential": 16,
                "cross_domain_transfer": 0,
            },
            "reproduction_level": {"level": 2, "label": "run official demo"},
            "rtx5080_experiment": {
                "artifact_root": "/home/jnln3799/research-artifacts/weekly-paper-lab/2026-W19-agent-memory",
                "minimum_viable_experiment": "Run the official demo on a tiny fixture.",
                "commands": ["python demo.py --small"],
                "metrics": ["runtime", "memory"],
                "stop_conditions": ["demo exceeds local GPU memory"],
            },
            "failure_taxonomy": {
                "engineering": [],
                "data": [],
                "evaluation": [],
                "theory": [],
                "hardware": [],
                "environment": [],
                "cost": [],
                "problem_definition": [],
            },
            "research_question_seed": {
                "question": "",
                "contribution_hypothesis": "",
                "next_idea_action": "none",
            },
            "idea_links": ["idea_000001"],
            "idea_connections": [
                {
                    "idea_id": "idea_000001",
                    "idea_path": "ideas/structured/idea_000001_example.yaml",
                    "relationship_type": "synthesis_seed",
                    "expected_use": "Use as a small test connection.",
                    "connection_strength": {
                        "score": 100,
                        "rule_version": "paper_connection_rubric_v2",
                        "dimensions": {
                            "topical_alignment": {
                                "score": 20,
                                "evidence": {
                                    "title_keyword_overlaps": ["agent", "memory", "workflow", "review"],
                                    "shared_tags": ["ai", "workflow", "review", "fixture"],
                                    "explicit_topic_match": True,
                                },
                            },
                            "method_workflow_alignment": {
                                "score": 20,
                                "evidence": {
                                    "shared_methods": ["audit loop", "fixture"],
                                    "shared_workflow_stages": ["read", "review"],
                                    "same_artifact_type": True,
                                    "same_failure_mode": True,
                                },
                            },
                            "next_step_impact": {
                                "score": 20,
                                "evidence": {
                                    "directly_updates_next_step": True,
                                    "produces_required_artifact": True,
                                    "reduces_open_uncertainties": ["scope", "metric"],
                                    "actionable_within_one_week": True,
                                },
                            },
                            "metric_baseline_support": {
                                "score": 20,
                                "evidence": {
                                    "shared_metrics": ["time", "precision"],
                                    "provides_baseline": True,
                                    "provides_fixture": True,
                                    "measurable_success_condition": True,
                                },
                            },
                            "research_generation_value": {
                                "score": 20,
                                "evidence": {
                                    "new_tests": ["test one", "test two"],
                                    "synthesis_paths": ["path one", "path two"],
                                    "can_update_yaml_record": True,
                                    "can_be_reference_citation": True,
                                },
                            },
                        },
                    },
                }
            ],
            "synthesis_assessment": {
                "rule_version": "paper_synthesis_rubric_v1",
                "synthesis_score": 20,
                "reference_role": "method_reference",
                "candidate_research_method": "Use the paper as a synthetic method seed.",
                "combine_with_idea_ids": ["idea_000001"],
                "required_followups": ["Run a small fixture."],
                "evidence": {
                    "has_transferable_method": True,
                    "has_measurable_fixture": True,
                    "links_two_or_more_ideas": True,
                    "defines_new_baseline_or_metric": True,
                    "can_be_cited_as_reference": True,
                },
            },
            "project_links": [],
            "planning_sync": {
                "status": "not_synced",
                "capacity_note": "none",
                "canonical_path": "weekly-paper-lab/papers/2026-W19-agent-memory/paper.yaml",
                "linked_idea_ids": ["idea_000001"],
            },
        }


if __name__ == "__main__":
    unittest.main()
