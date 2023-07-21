# tic_tac_toe/logic/validators.py
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tic_tac_toe.logic.models import GameState, Grid

import re

def validate_grid(grid: Grid) -> None:
    if not re.match(r"[\sX0]{9}$", grid.cells):
        raise ValueError("MUST CONTAIN 9 CELLS OF: X, O, OR SPACE")
    
def validate_game_state(game_state: GameState) -> None:
    validate_num_plays(game_state.grid)
    validate_start_plays(game_state.grid, game_state.start_play)
    validate_winner(game_state.grid, game_state.start_play, game_state.winner)

def validate_num_plays(grid: Grid) -> None:
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("WRONG NUMBER OF X'S AND O'S")