"""Game mode classes"""

# IMPORTS #
from itertools import cycle

# LOCAL IMPORTS #
from abstracts import IPlayer, IWinChecker
from board import RectangularBoard

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))     


# TODO: CHECK THIS DECORATOR
def check_on_match(func):
    def _decorator(self, *args, **kwargs):
        if self.acting:
            return func(self, *args, **kwargs)
    return _decorator



class OneVsOne:
    """One player vs one player"""
    def __init__(self) -> None:
        self.board = None
        self.win_checker = None
        self.score_to_win = None
        self.players = []
        self.on_match = False
    

    def set_board(self, rows: int, columns: int) -> None:
        self.board = RectangularBoard(rows, columns)


    def set_win_checker(self, win_checker_class: IWinChecker) -> bool:
        if not self.board:
            return False
        win_checker = win_checker_class()
        self.board.add_subscriber(win_checker)
        self.win_checker = win_checker()
        return True


    def set_score_to_win(self, value: int) -> None:
        self.score_to_win = value


    def set_players(self, players_list: list[IPlayer]) -> bool:
        if len(players_list) != 2:
            return False
        self.players = players_list
        return True

    
    def switch_match(self) -> bool:
        self.on_match = not self.on_match
        return self.on_match
        

    # TODO: IMPLEMENT MATCH WITHOUT LOOP
    
        