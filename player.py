"""Player concrete classes"""
# IMPORTS #
from random import randint

# LOCAL IMPORTS #
from abstracts import IPlayer

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))

"""
is a player
connect to the game
colect game rules

act when the game calls
when the game calls:
    receive board
    decide where to play and tell the game the coordinates
"""
class EasyPlayer(IPlayer):
    """Play on a random place of the board"""
    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark


    # TODO: ADD THE SELF.BOARD_STATE
    # TODO: ADD A WAY TO RECEIVE UPDATES FROM THE BOARD (OR FROM THE GAME)
    def play(self) -> tuple[int, int]:
        possible_plays = self._get_empty_places()
        return possible_plays[randint(0, len(possible_plays) - 1)]


    def _get_empty_places(self) -> list[tuple[int, int]]: # sourcery skip: for-append-to-extend
        empty_places = []
        for row_idx, row in enumerate(self.board_state):
            for column_idx, column in enumerate(row):
                if column is None:
                    empty_places.append((row_idx, column_idx))



def main(): 
    return


if __name__ == '__main__': 
    main()