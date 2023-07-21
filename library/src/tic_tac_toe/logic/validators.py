# tic_tac_toe/logic/validators.py
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tic_tac_toe.logic.models import Grid

import re

def validate_grid(grid: Grid) -> None:
    if not re.match(r"[\sX0]{9}$", grid.cells):
        raise ValueError("MUST CONTAIN 9 CELLS OF: X, O, OR SPACE")