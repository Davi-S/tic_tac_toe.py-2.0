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
        self.board_state: BOARD_HINT = None

    @abstractmethod
    def play(self) -> tuple[int, int]:
        pass

    def set_board(self, board_instance: Board2D):
        self.board_state = board_instance.board

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


class HumanPlayer(IPlayer):
    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, mark)

    def play(self) -> tuple[int, int]:
        """Get row and column from user input

        Returns:
            tuple[int, int]: row and column
        """
        # changing ranges to better user friendly
        while True:
            row = get_int_max('row: ', range(1, len(self.board_state) + 2))
            if not row:
                continue

            column = get_int_max('column: ', range(1, len(self.board_state) + 2))
            if not column:
                continue

            if (row, column) not in self._get_empty_places():
                print('Chosse a empty place')
                sleep(2)
                continue
            break
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


# TODO: make other dificults


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
