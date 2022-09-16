"""Board concrete classes"""

# IMPORTS #

# LOCAL IMPORTS #
from abstracts import IBoard, IBoardSubscriber

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


class RectangularBoard(IBoard):
    """Two dimensional array"""
    def __init__(self, rows: int, columns: int) -> None:
        self._board: list[list] = super()._create_board(rows, columns)
        self._subscribers: list[IBoardSubscriber] = []


    @property
    def board(self) -> list[list]:
        return self._board


    def place_mark(self, row: int, column: int, mark: str, rewrite: bool = False) -> bool:
        """Place a mark on the board

        Args:
            line (int): x axis
            column (int): y axis
            mark (str): The mark to place
            rewrite (bool, optional): Replace the current mark with the selected one. Defaults to False.

        Returns:
            bool: True if the marks was sucessfuly placed. False if the mark could not be placed
        """
        if rewrite or self._board[row][column] is None:
            self._board[row][column] = mark
            self.notify_subscribers(self._board)
            return True
        return False

    
    def add_subscriber(self, subscriber: IBoardSubscriber) -> None:
        """Add an subscriber to the publisher."""
        self._subscribers.append(subscriber)


    def remove_subscriber(self, subscriber: IBoardSubscriber) -> None:
        """Remove an subscriber from the publisher."""
        self._subscribers.remove(subscriber)


    def notify_subscribers(self, board_state: list[list]) -> None:
        """Notify all subscribers about an event.

        Args:
            board_state (list[list]): The board state to change on the subscribers
        """
        for subscriber in self._subscribers:
            subscriber.update_board_state(board_state)


def main() -> None:
    return


if __name__ == '__main__': 
    main()