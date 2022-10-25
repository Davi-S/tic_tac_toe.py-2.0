"""Abstractions"""

# standard library imports #
import abc

# related third party imports #
# local application/library specific imports #
import engine.board as bd


class IWinChecker(abc.ABC):
    """Gets a board state to check for wins"""
    def __init__(self, board_state: bd.BOARD_HINT) -> None:
        self.board_state: bd.BOARD_HINT = board_state  # The board state to check for wins

    @abc.abstractmethod
    def check_win(self) -> bool:
        pass

    @abc.abstractmethod
    def win_info(self) -> dict:
        pass


class IGame(abc.ABC):
    """"""
    board: bd.Board
    win_checker: IWinChecker

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
