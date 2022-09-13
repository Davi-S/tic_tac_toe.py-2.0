# IMPORTS #
from abc import ABC, abstractmethod, NotImplementedError

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


# TODO: IMPLEMENT THIS CLASSES


class WinChecker(ABC):
    """
    check if the win condition is true on the board
    send win info to the game
    """
    pass


class ClassicalWinChecker(WinChecker):
    """a line, column of great diagonal fully filled with one mak"""
    pass
        

# TODO: MAKE CLASSES AND USE THIS FUNCTIONS 

# ### WIN RELATED METHODS ###
# def check_win(self) -> bool:
#     """Check if there is a win on the board

#     Returns:
#         bool: True if there is a win, otherwise, False
#     """
#     return self.get_winner() != self._default_value


# def get_winner(self) -> str:
#     """Get the mark that won in any place of the board.
#     If none won, return the board._default_value"""
#     # Only getting the mark info
#     mark = {self.get_win_info().values()}
#     mark.remove(self._default_value)
#     return mark if len(mark) == 1 else self._default_value


# def get_win_info(self) -> dict:
#     """Get the group info from the board

#     Returns:
#         dict: The info for each group
#     """
#     return {'row':self._get_row_winner(),
#             'column':self._get_column_winner(),
#             'diagonal':self._get_diagonal_winner()}


# def _check_win_condition(self, group: list, mark: str) -> bool:
#     """Check if the given group has consecutives occourences of the given mark to occour a win.
#     The group can be a row, column or diagonal.
#     If the mark is the defalt value, False is retured"""
#     return (mark != self._default_value) and \
#             (helpers.longest_consecutive_occourence(group, mark) >= self._win_sequence_size)


# def _get_row_winner(self) -> tuple[str, int]:
#     """Return the mark that won on any row of the board.
#     If none won, return the default value and a negative index

#     Returns:
#         tuple[str, int]: str: the mark that won. int: index of the row won
#     """
#     for idx, row in enumerate(helpers.Matrix.rows(self._board)):
#         for mark in set(row):
#             if self._check_win_condition(row, mark):
#                 return mark, idx
#     return self._default_value, -1


# def _get_column_winner(self) -> tuple[str, int]:
#     """Return the mark that won on any column of the board.
#     If none won, return the default value and a negative index

#     Returns:
#         tuple[str, int]: str: the mark that won. int: index of the column won
#     """
#     for idx, column in enumerate(helpers.Matrix.columns(self._board)):
#         for mark in set(column):
#             if self._check_win_condition(column, mark):
#                 return mark, idx
#     return self._default_value, -1


# def _get_diagonal_winner(self) -> tuple[str, int]:
#     """Return the mark that won on any diagonal of the board.
#     If none won, return the default value and a negative index

#     Returns:
#         tuple[str, int]: str -> the mark that won. int -> index of the diagonal won:
#         0 for the primary diagonal and 1 for the secundaty diagonal
#     """        
#     # Primary diagonal
#     for idx, diagonal in enumerate(helpers.Matrix.p_diagonal(self._board)):
#         for mark in diagonal:
#             if self._check_win_condition(diagonal, mark):
#                 return mark, idx

#     # Secondary diagonal
#     for idx, diagonal in enumerate(helpers.Matrix.s_diagonal(self._board)):
#         for mark in diagonal:
#             if self._check_win_condition(diagonal, mark):
#                 return mark, idx

#     return self._default_value, -1
