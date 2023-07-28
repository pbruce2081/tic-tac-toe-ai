# tic_tac_toe/game/players.py

import abc

from logic.exceptions import InvalidMove
from logic.models import GameState, Play, Move

class Player(metaclass=abc.ABCMeta):
    def __init__(self, play: Play) -> None:
        self.play = play

    def make_move(self, game_state: GameState) -> GameState:
        if self.play is game_state.curr_play:
            if move:
                move = self.get_move(game_state):
