# tic_tac_toe/game/players.py

import abc

from logic.exceptions import InvalidMove
from logic.models import GameState, Play, Move

class Player(metaclass=abc.ABCMeta):
    def __init__(self, play: Play) -> None:
        self.play = play