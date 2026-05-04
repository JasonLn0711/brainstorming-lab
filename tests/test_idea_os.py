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
                "top_n": 3,
                "similarity_threshold": 0.5,
            },
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
            "selection_001": {
                "id": "idea_000001",
                "title": "Planning bridge",
                "status": "structured",
                "score": 12,
                "next_step": "Run a tiny test.",
                "path": "ideas/structured/idea_000001_planning_bridge.yaml",
            }
        }
        first = insert_or_replace_block("# Daily note\n", render_today_block(selection))
        second = insert_or_replace_block(first, render_today_block(selection))
        self.assertEqual(first, second)
        self.assertEqual(second.count("<!-- IDEA_OS_TODAY_START -->"), 1)

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
