"""Guard single-read paper validation and quality-record identity handoff."""
import tempfile
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from idea_os.paper_lab import validate_paper_folder
from idea_os import paper_shortlist


class PaperLoadingTests(unittest.TestCase):
    def test_shortlist_batch_reads_each_document_once_without_stale_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            lab = root / "weekly-paper-lab"
            shortlists = lab / "shortlists"
            shortlists.mkdir(parents=True)
            paper = lab / "papers" / "prior" / "paper.yaml"
            paper.parent.mkdir(parents=True)
            paper.write_text(json.dumps({"week": "2026-W18", "paper_id": "unrelated"}))
            for week in ("2026-W19", "2026-W20"):
                data = {"week": week, "rubric_version": "paper_lab_rubric_v1",
                        "cycle_slot": "main_a", "candidates": [
                            {"paper_id": f"{week}-{i}", "selected": i == 0,
                             "evidence_sources": {}, "scores": {}} for i in range(3)]}
                (shortlists / f"{week}.yaml").write_text(json.dumps(data))
            # Use a deterministic loader to isolate read reuse from YAML syntax.
            def load(path):
                return json.loads(path.read_text())
            with patch.object(paper_shortlist, "load_yaml", side_effect=load) as loader:
                expected = [error for path in paper_shortlist.shortlist_paths(root)
                            for error in paper_shortlist.validate_shortlist_file(path, root)]
                self.assertEqual(loader.call_count, 8)
                loader.reset_mock()
                self.assertEqual(paper_shortlist.validate_shortlists(root), expected)
                self.assertEqual(loader.call_count, 3)
                paper.write_text(json.dumps({"week": "2026-W18", "paper_id": "2026-W19-0"}))
                loader.reset_mock()
                changed = paper_shortlist.validate_shortlists(root)
                self.assertEqual(loader.call_count, 3)
                self.assertTrue(any("already selected before" in error for error in changed))
                self.assertNotEqual(changed, expected)

    def test_one_parse_with_identity_and_error_preservation(self):
        cases = [({"paper_id": "paper-1"}, "paper-1", None),
                 ({}, "", None), ([], None, "must be a mapping"),
                 (ValueError("invalid fixture"), None, "could not parse YAML")]
        for parsed, identity, error in cases:
            with self.subTest(parsed=parsed), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp).resolve()
                folder = root / "2026-W45-fixture"
                folder.mkdir()
                source = folder / "paper.yaml"
                source.write_text("fixture", encoding="utf-8")
                with patch("idea_os.paper_lab.load_yaml") as load, \
                     patch("idea_os.paper_lab.validate_paper_record", return_value=["domain finding"]) as record, \
                     patch("idea_os.paper_lab.validate_quality_evaluation_file", return_value=["quality finding"]) as quality:
                    if isinstance(parsed, Exception):
                        load.side_effect = parsed
                    else:
                        load.return_value = parsed
                    errors = validate_paper_folder(folder, root)
                    load.assert_called_once_with(source)
                    quality.assert_called_once_with(folder / "scientific_evaluation.yaml", root, identity)
                    self.assertIn("quality finding", errors)
                    if error:
                        self.assertTrue(any(error in item for item in errors))
                        record.assert_not_called()
                    else:
                        record.assert_called_once_with(parsed, folder, root)
                        self.assertIn("domain finding", errors)

    def test_missing_paper_does_not_load_or_infer_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            with patch("idea_os.paper_lab.load_yaml") as load, \
                 patch("idea_os.paper_lab.validate_quality_evaluation_file", return_value=[]) as quality:
                errors = validate_paper_folder(root, root)
                load.assert_not_called()
                self.assertTrue(any("missing paper.yaml" in item for item in errors))
                self.assertIsNone(quality.call_args.args[2])
