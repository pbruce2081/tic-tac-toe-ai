# tic_tac_toe/logic/models.py

import enum
from dataclasses import dataclass

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