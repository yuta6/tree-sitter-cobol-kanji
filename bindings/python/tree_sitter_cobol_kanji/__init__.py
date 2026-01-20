"""Tree-sitter COBOL Kanji grammar."""

from tree_sitter import Language
import tree_sitter_cobol_kanji._binding as _binding


def language():
    """Get the tree-sitter Language for COBOL Kanji."""
    return Language(_binding.language())


__all__ = ["language"]
