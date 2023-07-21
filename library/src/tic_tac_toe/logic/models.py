# tic_tac_toe/logic/models.py

import enum

class Play(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Play":
        if self is Play.NAUGHT:
            return Play.CROSS
        else:
            return Play.NAUGHT