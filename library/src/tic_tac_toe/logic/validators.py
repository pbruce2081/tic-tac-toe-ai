# tic_tac_toe/logic/validators.py
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tic_tac_toe.logic.models import GameState, Grid, Play

import re

from .exceptions import InvalidGameState

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

def validate_start_plays(grid: Grid, start_play: Play) -> None:
    if grid.x_count > grid.o_count:
        if start_play != "X":
            raise InvalidGameState("WRONG STARTING PLAY")
    elif grid.o_count > grid.x_count:
        if start_play != "O":
            raise InvalidGameState("WRONG STARTING PLAY")
        
def validate_winner(grid: Grid, start_play: Play, winner: Play | None) -> None:
    if winner == "X":
        if start_play == "X":
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("WRONG NUMBER OF X'S")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("WRONG NUMBER OF X'S")
    elif winner == "O":
        if start_play == "O":
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("WRONG NUMBER OF O'S")
        else:
            if grid.o_count != grid.x_count:
                raise InvalidGameState("WRONG NUMBER OF O'S")