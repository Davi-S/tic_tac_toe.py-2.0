"""Game mode classes"""

# IMPORTS #
from itertools import cycle

# LOCAL IMPORTS #
from abstracts import BOARD_HINT, IBoard, IPlayer
from board import Board2D
from win_check import ClassicWinChecker

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


# TODO: IMPLEMET ABSTRACT FOR GAME MODES
class ClassicGameMode:
    def __init__(self, player_list: list[IPlayer]) -> None:
        self.rows = 3
        self.columns = 3
        self.board = Board2D
        self.win_checker = ClassicWinChecker
        self.score_to_win = 3
        self.players: list[IPlayer] = player_list

    def create_board_instance(self) -> IBoard:
        return self.board(self.rows, self.columns)


# TODO: TEST THIS CLASS
class Match(ClassicGameMode):
    def __init__(self) -> None:
        self.match_board: IBoard = None
        self.act_player: IPlayer = None

    def start_match(self) -> bool:
        self.match_board = super().create_board_instance()
        self.act_player = super().players[0]

    def _next_player(self) -> IPlayer:
        yield from cycle(super().players)
    
    def next_player(self) -> IPlayer:
        self.act_player = self._next_player()
    
    def check_win(self) -> bool:
        return super().win_checker(self.match_board.board).check_win()

    def get_win_info(self) -> dict:
        return super().win_checker(self.match_board.board).get_win_info()


def main():
    return


if __name__ == '__main__':
    main()