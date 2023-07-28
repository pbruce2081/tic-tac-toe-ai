# frontend/console/frontend-renderers.py

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState

class ConsoleRenderer(Renderer):
    def render_frontend(self, game_state: GameState) -> None:
        clear_screen()
    
def clear_screen() -> None:
    print("\033c", end="")