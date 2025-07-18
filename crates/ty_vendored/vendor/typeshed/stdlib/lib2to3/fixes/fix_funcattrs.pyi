"""
Fix function attribute names (f.func_x -> f.__x__).
"""

from typing import ClassVar, Literal

from .. import fixer_base

class FixFuncattrs(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[str]
    def transform(self, node, results) -> None: ...
