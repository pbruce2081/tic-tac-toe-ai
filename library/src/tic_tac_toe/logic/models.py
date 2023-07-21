# tic_tac_toe/logic/models.py

import enum
from dataclasses import dataclass
import re
from functools import cached_property

WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
    "?...?...?",
    "..?.?.?.."
)

class Play(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Play":
        if self is Play.NAUGHT:
            return Play.CROSS
        else:
            return Play.NAUGHT

@dataclass(frozen=True)
class Grid:
    # create the number of cells in the grid
    cells: str = " " * 9

    def __post_init__(self) -> None:
        if not re.match(r"^[\sX0]{9}$", self.cells):
            raise ValueError("MUST CONTAIN 9 CELLS OF: X, O, OR SPACE")
    
    @cached_property
    # count how many X's there are
    def x_count(self) -> int:
        return self.cells.count("X")
    
    @cached_property
    # count how many O's there are
    def o_count(self) -> int:
        return self.cells.count("O")
    
    @cached_property
    # count how many empty cells there are
    def empty_count(self) -> int:
        return self.cells.count(" ")

@dataclass(frozen=True)
class Move:
    play: Play
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

@dataclass(frozen=True)
class GameState:
    grid: Grid
    start_play: Play = Play("X")

    @cached_property
    def curr_play(self) -> Play:
        # check if the number of X's is the same as the number of O's
        if self.grid.x_count == self.grid.o_count:
            # return X
            return self.start_play
        else:
            # return O
            return self.start_play.other
    
    @cached_property
    def game_started(self) -> bool:
        # return whether the grid is empty or not (game started or not)
        return self.grid.empty_count == 9
    
    @cached_property
    def game_over(self) -> bool:
        # return whether there is a winner or a tie
        return self.winner is not None or self.tie
    
    @cached_property
    def tie(self) -> bool:
        # return whether the game ended in a tie
        return self.winner is None and self.grid.empty_count == 0
    
    @cached_property
    def winner(self) -> Play or None:
        # iterate through all winning patterns
        for pattern in WINNING_PATTERNS:
            # iterate through all plays
            for play in Play:
                if re.match(pattern.replace("?", play), self.grid.cells):
                    return play
        return None