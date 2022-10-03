"""Player concrete classes"""

# IMPORTS #
from random import randint
from abc import ABC, abstractmethod

from markupsafe import Markup

# LOCAL IMPORTS #
from board import BOARD_HINT, Board2D
from helpers import type_menu

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


class IPlayer(ABC):
    """A player of the game. Receives a board state and chose where to play."""

    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark
        self.board_instance = None

    @abstractmethod
    def play(self) -> tuple[int, int]:
        pass

    def set_board(self, board_instance: Board2D):
        self.board_instance = board_instance


class HumanPlayer(IPlayer):
    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, Markup)


    def play(self):
        row = type_menu('Place mark', 'row: ')
        column = type_menu('Place mark', 'column: ')
        return row, column


class EasyPlayer(IPlayer):
    """Play on a random place of the board"""

    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, mark)

    def play(self) -> tuple[int, int]:
        """Choose a random empty coordinate from the board

        Returns:
            tuple[int, int]: The coordinate chosen
        """
        possible_plays = self._get_empty_places()
        return possible_plays[randint(0, len(possible_plays) - 1)]

    def _get_empty_places(self) -> list[tuple[int, int]]:  # sourcery skip: for-append-to-extend
        """Get the board empty places

        Returns:
            list[tuple[int, int]]: List of Empty coordinates
        """
        empty_places = []
        for row_idx, row in enumerate(self.board_state):
            for column_idx, column in enumerate(row):
                if column is None:
                    empty_places.append((row_idx, column_idx))
        return empty_places


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
