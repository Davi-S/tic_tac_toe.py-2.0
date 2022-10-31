"""Abstractions"""

# standard library imports #
import abc

# related third party imports #
# local application/library specific imports #
import engine.board as bd
from engine.win_check import WinChecker


class IGame(abc.ABC):
    """"""
    board: bd.Board
    win_checker: WinChecker

    @abc.abstractmethod
    def run() -> None:
        pass


class IPlayer(abc.ABC):
    """A player of the game. Receives a board state and chose where to play."""

    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark
        self.game_instance = None

    def set_game(self, game_instance: IGame) -> None:
        self.game_instance = game_instance
