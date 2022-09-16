"""Player concrete classes"""

# IMPORTS #
from random import randint

# LOCAL IMPORTS #
from abstracts import IPlayer

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

    def update_board_state(self, board_state: list[list]) -> None:
        """Update the board state. This method is used by a IPublisher

        Args:
            board_state (list[list]): The board state
        """
        self.board_state = board_state

    def play(self) -> tuple[int, int]:
        """Choose a random empty coordinate from the board

        Returns:
            tuple[int, int]: The coordinate chosen
        """
        possible_plays = self._get_empty_places()
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



def main(): 
    return


if __name__ == '__main__': 
    main()