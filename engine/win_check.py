"""WinCheker concrete classes"""

# IMPORTS #

# LOCAL IMPORTS #
from helpers import Matrix
from board import BOARD_HINT

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


class ClassicWinChecker:
    """A row, column of great diagonal if fully filled with only one mark"""
    def __init__(self, board_state: BOARD_HINT) -> None:
        self.board_state: BOARD_HINT = board_state  # The board state to check for wins


    def check_win(self) -> bool:
        """Check if there is a win on the game

        Returns:
            bool: True is there is a win. False is there is no win
        """
        win_info = self.get_win_info()
        return any(value[0] != None for value in win_info.values())


    def get_win_info(self) -> dict:
        """The information about a win

        Returns:
            dict: {group: (mark, index)}
        """
        return {'row':self._get_row_winner(), 'column':self._get_column_winner(), 'diagonal':self._get_diagonal_winner()}
    

    def _win_condition(self, group: list) -> bool:
        """Check if the win condition is true

        Args:
            group (list): A row, column or great diagonal of the board state

        Returns:
            bool: True is the win condition is true. False if the win condition is false
        """
        return len(set(group)) == 1 and set(group) != {None}



    def _get_row_winner(self) -> tuple[str | None, int]:  # sourcery skip: use-next
        """Return the mark that won on any row of the board.
        If none won, return None and a negative index

        Returns:
            tuple[str, int]: str: the mark that won. int: index of the row won
        """
        for idx, row in enumerate(Matrix.rows(self.board_state)):
            if self._win_condition(row):
                return row[0], idx  # return the mark and the index of the row where it won
        return None, -1


    def _get_column_winner(self) -> tuple[str | None, int]:  # sourcery skip: use-next
        """Return the mark that won on any column of the board.
        If none won, return None and a negative index

        Returns:
            tuple[str, int]: str: the mark that won. int: index of the column won
        """
        for idx, column in enumerate(Matrix.columns(self.board_state)):
            if self._win_condition(column):
                return column[0], idx  # return the mark and the index of the column where it won
        return None, -1


    def _get_diagonal_winner(self) -> tuple[str | None, int]:
        """Return the mark that won on any diagonal of the board.
        If none won, return None and a negative index

        Returns:
            tuple[str, int]: str -> the mark that won. int -> index of the diagonal won:
            0 for the primary diagonal and 1 for the secundary diagonal
        """
        # Primary diagonal
        great_diagonal = max(Matrix.p_diagonal(self.board_state), key=len)
        if self._win_condition(great_diagonal):
            return great_diagonal[0], 0

        # Secondary diagonal
        great_diagonal = max(Matrix.s_diagonal(self.board_state), key=len)
        if self._win_condition(great_diagonal):
            return great_diagonal[0], 1
        return None, -1


def main() -> int:
    return 0


if __name__ == '__main__': 
    main()