"""Board concrete classes"""

# IMPORTS #

# LOCAL IMPORTS #

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


BOARD_HINT = list[list]


class Board2D:
    """Two dimensional array"""

    def __init__(self, rows: int, columns: int) -> None:
        self._board: BOARD_HINT = self._create_board(rows, columns)
        # TODO: CHECK IF TIME LINE IS WORKING
        self.time_line: list[BOARD_HINT] = []

    @property
    def board(self) -> BOARD_HINT:
        return self._board

    def place_mark(self, row: int, column: int, mark: str, rewrite: bool = False) -> bool:
        """Place a mark on the board

        Args:
            line (int): x axis
            column (int): y axis
            mark (str): The mark to place
            rewrite (bool, optional): Replace the current mark with the selected one. Defaults to False.

        Returns:
            bool: True if the marks was sucessfuly placed. False if the mark could not be placed
        """
        if rewrite or self._board[row][column] is None:
            self._board[row][column] = mark
            # append to time_line
            self.time_line.append(self._board)
            return True
        return False

    def _create_board(self, rows: int, columns: int) -> BOARD_HINT:
        """Create a empty two dimention matrix (board)"""
        gridline = [None for _ in range(rows)]
        gridline = [list(gridline) for _ in range(columns)]
        return gridline


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
