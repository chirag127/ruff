"""
Fix incompatible imports and module references.
"""

from _typeshed import StrPath
from collections.abc import Generator
from typing import ClassVar, Final, Literal

from .. import fixer_base
from ..pytree import Node

MAPPING: Final[dict[str, str]]

def alternates(members): ...
def build_pattern(mapping=...) -> Generator[str, None, None]: ...

class FixImports(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    mapping = MAPPING
    def build_pattern(self): ...
    def compile_pattern(self) -> None: ...
    def match(self, node): ...
    replace: dict[str, str]
    def start_tree(self, tree: Node, filename: StrPath) -> None: ...
    def transform(self, node, results) -> None: ...
