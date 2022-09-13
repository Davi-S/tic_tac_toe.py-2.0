# IMPORTS #
from abstracts import Board

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))

 
class TicTacToeBoard(Board):
    def __init__(self, rows: int=3, columns: int=3) -> None:
        """
        Args:
            rows (int, optional): Amount of row. Defaults to 3.
            columns (int, optional): Amount of columns. Defaults to 3.
        """
        self._rows = rows
        self._columns = columns
        self.board: list[list] = None


    def set_board(self, board: list[list]=None) -> None:
        """Set a new board.
        If no board is given, a new one is created with the values provide on the instace creation.
        The pre defined board should have, preferably, the amount of rows and columns provided on the class instace creation; if not, errors may occur.

        Args:
            board (list[list], optional): A pre defined board. Defaults to None.
        """
        if board:  # Pre defined board (for development usage)
            self.board = board
            return
        self.board = super()._create_board(self._rows, self._columns)


    def place_mark(self, row: int, column: int, mark: str, rewrite: bool=False) -> bool:
        """Place a mark on the board

        Args:
            line (int): x axis
            column (int): y axis
            mark (str): The mark to place
            rewrite (bool, optional): Replace the current mark with the selected one. Defaults to False.

        Returns:
            bool: True if the marks was sucessfuly placed. False if the mark could not be placed
        """
        # If rewrite is true, or, rewrite is false but the place does not have a mark already...
        if rewrite or ((not rewrite) and (not self._is_marked(row, column))):
            self.board[row][column] = mark
            return True
        else:
            return False
    

    def _is_marked(self, row: int, column: int) -> bool:
        """Checks if a place on the board has a mark on it

        Args:
            row (int): The row to check 
            column (int): The column to check

        Returns:
            bool: True if the place has a mark. False if the place does not have a mark
        """
        return self.board[row][column] != None


def main():
    return


if __name__ == '__main__': 
    main()