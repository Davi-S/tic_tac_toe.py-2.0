"""Main file. Meant do be run"""

# First of all, setup logging configuration. This is only needed on the main file. Will affect all other log instances in other files
import logging
import logging.config
from logs.logging_configuration import CONFIG_DICT, create_file_handler
logging.config.dictConfig(CONFIG_DICT)
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))

# IMPORTS #

# LOCAL IMPORTS #
from game_modes import OneVsOne
from win_check import ClassicalWinChecker
from player import EasyPlayer


def main():
    game = OneVsOne()
    game.set_board(3, 3)
    game.set_win_checker(ClassicalWinChecker)
    game.set_score_to_win(3)
    players = [EasyPlayer('player 1', 'x'), EasyPlayer('Player 2', 'o')]
    game.set_players(players)
    return


if __name__ == '__main__':
    main()