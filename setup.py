from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os


class Build(build_ext):
    def run(self):
        # Ensure the parser.c is up to date
        if not os.path.exists("src/parser.c"):
            raise RuntimeError(
                "src/parser.c not found. Please run 'tree-sitter generate' first."
            )
        build_ext.run(self)


setup(
    ext_modules=[
        Extension(
            name="tree_sitter_cobol_kanji._binding",
            sources=[
                "bindings/python/tree_sitter_cobol_kanji/binding.c",
                "src/parser.c",
                "src/scanner.c",
            ],
            include_dirs=["src"],
            extra_compile_args=[
                "-std=c11",
                "-fPIC",
            ] if os.name != "nt" else ["/std:c11"],
        )
    ],
    cmdclass={"build_ext": Build},
)
