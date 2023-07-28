# frontend/console/frontend-renderers.py

import textwrap
from typing import Iterable

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState

class ConsoleRenderer(Renderer):
    def render_frontend(self, game_state: GameState) -> None:
        clear_screen()
        if game_state.winner:
            print_blinking_txt(game_state.grid.cells, game_state.winning_cells)
            print(f"{game_state.winner} WINS \N{party popper}")
        else:
            print_grid(game_state.grid.cells)
            if game_state.tie:
                print("NO ONE WINS THIS TIME \N{neutral face}")
    
def clear_screen() -> None:
    print("\033c", end="")

def blinking_txt(text: str) -> str:
    return f"\033[5m{text}\033[0m"

def print_blinking_txt(cells: Iterable[str], pos: Iterable[int]) -> None:
    mutable_cells = list(cells)
    for p in pos:
        mutable_cells[p] = blinking_txt(mutable_cells[p])
    print_grid(mutable_cells)

def print_grid(cells: Iterable[str]) -> None:
    print(
        textwrap.dedent(
            """\
             A   B   C
           ------------
        1 ┆  {0} │ {1} │ {2}
          ┆ ───┼───┼───
        2 ┆  {3} │ {4} │ {5}
          ┆ ───┼───┼───
        3 ┆  {6} │ {7} │ {8}
    """
        ).format(*cells)
    )