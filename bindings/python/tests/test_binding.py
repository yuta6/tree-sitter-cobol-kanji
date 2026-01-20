"""Basic tests for tree-sitter-cobol-kanji bindings."""

import unittest
from tree_sitter import Parser
from tree_sitter_cobol_kanji import language


class TestBinding(unittest.TestCase):
    def test_can_load_grammar(self):
        """Test that the grammar can be loaded."""
        lang = language()
        self.assertIsNotNone(lang)

    def test_can_parse_simple_cobol(self):
        """Test that we can parse a simple COBOL program."""
        parser = Parser()
        parser.language = language()

        source_code = b"""       identification division.
       program-id. test.
       procedure division.
       stop run."""

        tree = parser.parse(source_code)
        root_node = tree.root_node

        self.assertEqual(root_node.type, "start")
        self.assertGreater(root_node.child_count, 0)

    def test_can_parse_japanese_variables(self):
        """Test that we can parse Japanese variable names."""
        parser = Parser()
        parser.language = language()

        source_code = b"""       identification division.
       program-id. test.
       data division.
       working-storage section.
       01  \xe9\xa1\xa7\xe5\xae\xa2\xe5\x90\x8d pic x(20).
       01  \xe9\x87\x91\xe9\xa1\x8d pic 9(10).
       procedure division.
       stop run."""

        tree = parser.parse(source_code)
        root_node = tree.root_node

        # Should parse without errors
        self.assertEqual(root_node.type, "start")
        self.assertFalse(root_node.has_error)


if __name__ == "__main__":
    unittest.main()
