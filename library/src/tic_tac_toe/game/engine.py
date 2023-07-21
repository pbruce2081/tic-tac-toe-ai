# tic_tac_toe/game/engine.py

from dataclasses import dataclass
from logic.exceptions import InvalidMove
from logic.models import GameState, Grid, Play

@dataclass(frozen=True)
class TicTacToe:
    p1: Player
    p2: Player
    renderer: Renderer

    def play_game(self, start_play: Play = Play("X")) -> None:
        game_state = GameState(Grid(), start_play)
        
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_curr_player(game_state)

            try:
                game_state = player.move_maker(game_state)
            except InvalidMove:
                pass