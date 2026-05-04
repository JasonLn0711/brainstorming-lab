from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from idea_os.clustering_engine import build_clusters
from idea_os.graphing import build_graph
from idea_os.indexer import generate_indexes
from idea_os.models import classify_score, score_idea, validate_idea
from idea_os.planning import insert_or_replace_block, render_today_block
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

    def test_score_classification_and_validation(self) -> None:
        idea = make_template_idea("idea_000001", "Scoring test")
        idea["maturity"] = {"clarity": 4, "testability": 4, "connectedness": 3, "evidence": 2}
        score_idea(idea)
        self.assertEqual(idea["score"], 13)
        self.assertEqual(idea["status"], "structured")
        self.assertEqual(classify_score(20), "research_ready")
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

    def test_graph_cluster_and_research_candidate(self) -> None:
        ideas = [
            self._idea("idea_000001", "AI triage", 13, ["ai-triage"], ["idea_000002"]),
            self._idea("idea_000002", "Review triage", 15, ["ai-triage"], ["idea_000001"]),
            self._idea("idea_000003", "Loose note", 4, ["misc"], []),
        ]
        graph = build_graph(ideas, threshold=0.5)
        self.assertTrue(any("manual_connection" in edge["reasons"] for edge in graph["edges"]))

        clusters = build_clusters(ideas, threshold=0.5)
        self.assertGreaterEqual(clusters["cluster_001"]["size"], 2)

        candidates = generate_research_candidates(clusters, ideas)
        self.assertIn("research_candidate_01", candidates)

    def test_index_generation(self) -> None:
        idea = self._idea("idea_000001", "Indexed idea", 12, ["index"], [])
        path = path_for_idea(idea, self.root)
        save_idea(path, idea)
        loaded = dict(idea)
        loaded["_path"] = str(path)
        idea_index, tag_index = generate_indexes([loaded], self.root)
        self.assertIn("Indexed idea", idea_index.read_text(encoding="utf-8"))
        self.assertIn("index", tag_index.read_text(encoding="utf-8"))

    def test_planning_marker_idempotency(self) -> None:
        selection = {
            "selected": [
                {
                    "id": "idea_000001",
                    "title": "Planning bridge",
                    "selection_type": "exploit",
                    "selection_score": 1.5,
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
        self.assertIn("idea_000002", pools["exploitation_pool"])
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
  maturity_delta:
    clarity: 1
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
        self.assertEqual(updated["maturity"]["clarity"], 5)

    def _idea(self, idea_id: str, title: str, score: int, tags: list[str], connections: list[str]) -> dict:
        idea = make_template_idea(idea_id, title, tags=tags)
        idea["summary"] = f"{title} uses triage evidence routing and reviewer workflow."
        idea["problem_statement"] = "Given noisy inputs, select useful review targets."
        idea["connections"] = connections
        idea["maturity"] = {
            "clarity": min(5, score),
            "testability": 4 if score >= 12 else 1,
            "connectedness": 3 if connections else 0,
            "evidence": max(0, score - 12),
        }
        score_idea(idea)
        return idea


if __name__ == "__main__":
    unittest.main()
