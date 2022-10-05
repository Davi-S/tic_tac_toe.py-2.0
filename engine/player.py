"""Player concrete classes"""

# IMPORTS #
from random import randint
from abc import ABC, abstractmethod

# LOCAL IMPORTS #
from engine.board import Board2D, BOARD_HINT
from tui import get_int_max


class IPlayer(ABC):
    """A player of the game. Receives a board state and chose where to play."""

    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark
        self.board_state: BOARD_HINT = None

    @abstractmethod
    def play(self) -> tuple[int, int]:
        pass

    def set_board(self, board_instance: Board2D):
        self.board_state = board_instance.board


class HumanPlayer(IPlayer):
    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, mark)


    def play(self) -> tuple[int, int]:
        """Get row and column from user input

        Returns:
            tuple[int, int]: row and column
        """
        # changing ranges to better user friendly
        row = get_int_max('row: ', min=1, max=len(self.board_state) + 1) - 1
        column = get_int_max('column: ', min=1, max=len(self.board_state) + 1) - 1
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
