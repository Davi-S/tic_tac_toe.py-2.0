# IMPORTS #
from itertools import product
from abc import ABC, abstractmethod

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))

# TODO: CHECK IF THE BOARD CLASS IS CORRECTLY IMPLEMENTED
class Board(ABC):
    @property
    @abstractmethod
    def board(self):
        pass

    @abstractmethod
    def place_mark(self):
        pass

    @abstractmethod
    def set_board(self):
        pass

    def _create_board(self, default_value=None, x_axis: int=None, y_axis: int=None) -> list[list]:
        """Create a empty matrix"""
        gridline = [default_value for _ in range(x_axis)]
        gridline = [list(gridline) for _ in range(y_axis)]
        return gridline


# FIXME: REFACTOR THIS CLASS TO ATEND THE CHANGES    
class TicTacToeBoard(Board):
    """
    board instance
    place marks on the board
    get board info
    """
    def __init__(self, default_value: str = ' ', size: int = 3, win_sequence: int = None) -> None:
        self._default_value = default_value
        self._size = size
        self._win_sequence_size = self._size if win_sequence is None else win_sequence
        self._board: list[list] = None


    @property
    def board(self) -> list[list]:
        return self._board


    def set_board(self, board: list[list]=None) -> None:
        """Set a board
        if no board is given, a new one is created with the values provide on the instace creation

        Args:
            board (list[list], optional): a pre defined board. Preferably with the same x and y axis provided on the class instace creation; if not, errors may occour. Defaults to None.
        """
        if board:  # Pre defined board (for development usage)
            self._board = board
            return
        self._board = super()._create_board(self._default_value, self._size, self._size)  # square board

    
    def is_marked(self, row: int, column: int) -> bool:
        """Checks if a place on the board has a mark on it"""
        return self._board[row][column] != self._default_value


    def is_filled(self) -> bool:
            """Check if the board is fully filled"""
            return all(
                self.is_marked(row, column)
                for row, column in product(range(self._size), range(self._size)))
    

    def empty_spaces(self) -> int:
        """number of empty spaces on the board"""
        return sum(
            not self.is_marked(row, column)
            for row, column in product(range(self._size), range(self._size)))


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
        if rewrite or ((not rewrite) and (not self.is_marked(row, column))):
            self._board[row][column] = mark
            return True
        else:
            return False


class ClassicalBoard(Board):
    """The classical 3x3 board"""
    # TODO: INPLEMENT THIS CLASS
    pass


def main():
    board = TicTacToeBoard()
    print(board.board)
    return


if __name__ == '__main__': 
    main()