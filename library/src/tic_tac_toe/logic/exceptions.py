# tic_tac_toe/logic/exceptions.py

class InvalidGameState(Exception):
    """Raised when game state is invalid"""

class InvalidMove(Exception):
    """Raise when move is invalid"""