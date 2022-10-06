"""Player concrete classes"""

# IMPORTS #
from random import randint
from abc import ABC, abstractmethod
from time import sleep

# LOCAL IMPORTS #
from engine.board import Board2D, BOARD_HINT
from tui import get_int_max


class IPlayer(ABC):
    """A player of the game. Receives a board state and chose where to play."""

    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark
        self.board_instance: Board2D = None

    @abstractmethod
    def play(self) -> tuple[int, int]:
        pass

    def set_board(self, board_instance: Board2D):
        self.board_instance = board_instance


class HumanPlayer(IPlayer):
    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, mark)

    def play(self) -> tuple[int, int]:
        """Get row and column from user input

        Returns:
            tuple[int, int]: row and column
        """
        # changing ranges to better user friendly
        row = get_int_max('ROW: ', range(1, len(self.board_instance.board) + 2))
        column = get_int_max('COLUMN: ', range(1, len(self.board_instance.board) + 2))
        if isinstance(row, int) and isinstance(column, int):
            row, column = row-1, column-1
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
        possible_plays = self.board_instance.empty_places()
        return possible_plays[randint(0, len(possible_plays) - 1)]


# TODO: make other dificults


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
