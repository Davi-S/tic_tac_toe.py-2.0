# IMPORTS #
# LOCAL IMPORTS #

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


# TODO: IMPLEMENT THE TICTACTOEGAME CLASS
# TODO: EVERY TIME THAT THE BOARD CHANGES, THE GAME SHOULD UPDATE THE CLASSES REGISTERED ON THE OBSERVER FOR THIS
class TicTacToeGame:
    """
    manage the game
    define rules
    receive the players
    tell players the rules
    create the board as needed
    manage turns
    look at the board and show it to the players
    collects the coordinates of the player who is on turn
    tell the board where to place a mark
    verify wins using the win check (based on what is sees on the board, the players info mark, and rules)
    count score
    """
    pass
    
    
def main() -> None:    # sourcery skip: docstrings-for-functions
    test = [['x', 'o', 'o'],
            ['o', 'o', 'x'],
            ['x', 'x', 'o']]
    return


if __name__ == '__main__': 
    main()