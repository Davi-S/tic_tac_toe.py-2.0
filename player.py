# IMPORTS #
from abc import ABC

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


# TODO: IMPLEMENT THE PLAYERs CLASS


class Player(ABC):
    """
    is a player
    connect to the game
    colect game rules
    act when the game calls
    when the game calls:
        receive board
        decide where to play and tell the game the coordinates
    """
    pass


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