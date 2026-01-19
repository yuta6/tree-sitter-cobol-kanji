"""Tree-sitter COBOL Kanji grammar."""

from importlib.resources import files as _files

from tree_sitter import Language


def _get_library_path():
    return str(_files(__package__) / "tree_sitter_cobol_kanji.so")


def language():
    """Return the tree-sitter Language for COBOL Kanji."""
    return Language(_get_library_path(), "COBOL")


__all__ = ["language"]
