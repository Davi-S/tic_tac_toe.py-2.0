"""Board concrete classes"""

# IMPORTS #

# LOCAL IMPORTS #
from abstracts import IBoard

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))

 
class Board(IBoard):
    def __init__(self, rows:int, columns:int) -> None:
        self._rows = rows
        self._columns = columns
        self._board = super()._create_board(self._rows, self._columns)

    @property
    def board(self):
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
            return True
        return False
        

def main():
    return


if __name__ == '__main__': 
    main()