# tic_tac_toe/logic/validators.py

import re
from tic_tac_toe.logic.models import Grid

def validate_grid(grid: Grid) -> None:
    if not re.match(r"[\sX0]{9}$", grid.cells):
        raise ValueError("MUST CONTAIN 9 CELLS OF: X, O, OR SPACE")