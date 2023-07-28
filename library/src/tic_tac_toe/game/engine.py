# tic_tac_toe/game/engine.py

from dataclasses import dataclass
from typing import Callable, TypeAlias

from tic_tac_toe.game.players import Player
from logic.exceptions import InvalidMove
from logic.models import GameState, Grid, Play
from logic.validators import validate_players

ErrorHandler: TypeAlias = Callable[[Exception], None]

@dataclass(frozen=True)
class TicTacToe:
    p1: Player
    p2: Player
    renderer: Renderer

    def __post_init__(self):
        validate_players(self.p1, self.p2)

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
    
    def get_curr_player(self, game_state: GameState) -> Player:
        if game_state.curr_play is self.p1.play:
            return self.p1
        else:
            return self.p2