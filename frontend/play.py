# frontend/play.py

from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandComputerPlayer
from tic_tac_toe.logic.models import Play

from console.frontend_renderers import ConsoleRenderer

p1 = RandComputerPlayer(Play("X"))
p2 = RandComputerPlayer(Play("O"))

TicTacToe(p1, p2, ConsoleRenderer()).play()