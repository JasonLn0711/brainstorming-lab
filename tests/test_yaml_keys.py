"""Quoted mapping keys must survive files written by other YAML writers."""
import unittest
from unittest.mock import patch

from idea_os import yaml_io


class QuotedKeyTests(unittest.TestCase):
    def test_fallback_quoted_keys_and_embedded_colons(self):
        text = '''checklist:
  'yes': false
  "no": true
  'a:b': 3
  "c:d": 4
  'author''s': value
  "escaped\\\"key": text
items:
  - 'yes': true
    "no": false
'''
        expected = {"checklist": {"yes": False, "no": True, "a:b": 3,
                                  "c:d": 4, "author's": "value", 'escaped"key': "text"},
                    "items": [{"yes": True, "no": False}]}
        with patch.object(yaml_io, "_pyyaml", None):
            self.assertEqual(yaml_io.loads_yaml(text), expected)

    def test_malformed_quoted_keys_fail(self):
        for text in ['"yes: false', "'yes: false", '"yes" false', "'yes' false"]:
            with self.subTest(text=text), patch.object(yaml_io, "_pyyaml", None):
                with self.assertRaises(ValueError):
                    yaml_io.loads_yaml(text)

    def test_quoted_list_scalars_remain_scalars(self):
        with patch.object(yaml_io, "_pyyaml", None):
            self.assertEqual(yaml_io.loads_yaml('items:\n  - "a:b"\n  - \'yes\'\n'),
                             {"items": ["a:b", "yes"]})
