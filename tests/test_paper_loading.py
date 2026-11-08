"""Guard single-read paper validation and quality-record identity handoff."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from idea_os.paper_lab import validate_paper_folder


class PaperLoadingTests(unittest.TestCase):
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
