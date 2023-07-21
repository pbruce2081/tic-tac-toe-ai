# tic_tac_toe/logic/models.py

from __future__ import annotations

import enum
from dataclasses import dataclass
import re
from functools import cached_property

from .validators import validate_grid, validate_game_state
from .exceptions import InvalidMove

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
    def other(self) -> Play:
        if self is Play.NAUGHT:
            return Play.CROSS
        else:
            return Play.NAUGHT

@dataclass(frozen=True)
class Grid:
    # create the number of cells in the grid
    cells: str = " " * 9

    def __post_init__(self) -> None:
        validate_grid(self)
    
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

    def __post_init__(self) -> None:
        validate_game_state(self) 

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
    
    @cached_property
    def winning_cells(self) -> list[int]:
        # iterate through all winning patterns
        for pattern in WINNING_PATTERNS:
            # iterate through all plays
            for play in Play:
                if re.match(pattern.replace("?", play), self.grid.cells):
                    return[
                        match.start()
                        for match in re.finditer(r"\?", pattern)
                    ]
        return []
    
    @cached_property
    def poss_moves(self) -> list[Move]:
        # create a list of moves
        moves = []
        # check that the game is not over
        if not self.game_over:
            # iterate through all matches in the grid
            for match in re.finditer(r"\s", self.grid.cells):
                # add the moves to the list
                moves.append(self.move_maker(match.start()))
        return moves
    
    def move_maker(self, index: int) -> Move:
        if self.grid.cells[index] != " ":
            raise InvalidMove("CELL IS NOT EMPTY")
        return Move(
            play=self.curr_play,
            cell_index=index,
            before_state=self,
            after_state=GameState(
                Grid(
                    self.grid.cells[:index]
                    + self.curr_play
                    + self.grid.cells[index + 1:]
                ),
                self.start_play
            )
        )