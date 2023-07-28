# tic_tac_toe/game/renderers.py

import abc

from tic_tac_toe.logic.models import GameState

class Renderer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """RENDER THE CURRENT GAME STATE"""