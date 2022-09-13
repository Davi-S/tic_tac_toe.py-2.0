# THIS IS THE MAIN FILE, MEANT TO BE RUN
# First of all, setup logging configuration. This is only needed on the main file. Will affect all other log instances in other files
import logging
import logging.config
from logs.logging_configuration import CONFIG_DICT, create_file_handler
logging.config.dictConfig(CONFIG_DICT)

# IMPORTS #
from game import TicTacToeGame
from board import TicTacToeBoard
from player import HumanPlayer, CPUPlayer
from win_check import ClassicalWinChecker


# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


# TODO: CHECK IF THE GAME LOOP IDEA IS CORRECTLY IMPLEMENTED ->
# - ORDER OF THE CONFIGURATIONS
# - THE GAME CLASS SHOULD HAVE THE BOARD AND WINCHECKER AS PARAMETERS OR SHOLD CONFIGURATE IT ON THE MAIN LOOP?
# - THE GAME CLASS SHOULD HAVE MORE PARAMETERS FOR CONFIGURATION?
# - THE GAME CONFIGURATIONS SHOLD BE MADE INSIDE THE GAME CLASS OR OUTSIDE?
# - THE GAME CLASS SHOLD BE CREATED EACH TIME THAT THE USER WANT A NEW CONFIGURATION? (LIKE A NEW PLAYER OR A DIFERENT BOARD)

def main():
    # pick board
    board = TicTacToeBoard
    # Set board attributes
    board.size  #  The TicTacToeBoard usses a square board
    board.default_value
    ...

    # pick win_checker
    win_checker = ClassicalWinChecker
    # Set win cheker attributes
    game.win_checker.preference  
    ...

    # create the game with the board and win checker class
    game = TicTacToeGame(board, win_checker)

    # Set game "rules"
    game.game_mode  # certain score wins the game; infinite game; 
    game.score_mode  # win a match to score; win a amount of matches to score;
    ...

    # Add the players to the game
    game.add_player('Davi', 'x', HumanPlayer)
    game.add_player('PC', 'o', CPUPlayer)
    ...

    # start the round loop
    # while True:
        # show the board
        # player play
        # check win
        # change to next player

    # show the score
    # show options:
        # end
        # continue
        # change configuration
        # play again
        # (etc...)


    return


if __name__ == '__main__':
    main()