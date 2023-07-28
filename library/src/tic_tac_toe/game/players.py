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
                move = self.get_move(game_state)
                return move.after_state
            raise InvalidMove("NO MORE POSSIBLE MOVES")
        else:
            raise InvalidMove("IT'S THE OTHER PLAYER'S TURN")
    
    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Move or None:
        """RETURN THE CURRENT PLAYER'S MOVE IN THE GIVEN GAME STATE"""