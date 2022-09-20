"""Player concrete classes"""

# IMPORTS #
from random import randint

# LOCAL IMPORTS #
from abstracts import BOARD_HINT, IPlayer

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


class EasyPlayer(IPlayer):
    """Play on a random place of the board"""
    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, mark)
        self.board_state = None


    def play(self, board_state: BOARD_HINT) -> tuple[int, int]:
        """Choose a random empty coordinate from the board

        Returns:
            tuple[int, int]: The coordinate chosen
        """
        self.board_state = board_state
        possible_plays = self._get_empty_places()
        self.board_state = None
        return possible_plays[randint(0, len(possible_plays) - 1)]


    def _get_empty_places(self) -> list[tuple[int, int]]: # sourcery skip: for-append-to-extend
        """Get the board empty places

        Returns:
            list[tuple[int, int]]: List of Empty coordinates
        """
        empty_places = []
        for row_idx, row in enumerate(self.board_state):
            for column_idx, column in enumerate(row):
                if column is None:
                    empty_places.append((row_idx, column_idx))
        return empty_places



def main() -> int: 
    return 0


if __name__ == '__main__': 
    main()