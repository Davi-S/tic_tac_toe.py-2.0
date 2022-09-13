# IMPORTS #
from abstracts import Player

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


# TODO: IMPLEMENT THE PLAYER CLASS
class CPUPlayer(Player):
    """The CPU play the game"""
    pass


class HumanPlayer(Player):
    """A human player the game with inputs"""
    pass


def main():  
    return

if __name__ == '__main__': 
    main()