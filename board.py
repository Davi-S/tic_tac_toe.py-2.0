# IMPORTS #
from abstracts import IPublisher, ISubscriber, IBoard

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))

 
class TicTacToeBoard(IBoard, IPublisher):
    def __init__(self, rows: int = 3, columns: int = 3) -> None:
        """
        Args:
            rows (int, optional): Amount of row. Defaults to 3.
            columns (int, optional): Amount of columns. Defaults to 3.
        """
        self._rows = rows
        self._columns = columns
        self._board: list[list] = None
        self._subscribers = {}

    @property
    def board(self) -> list[list]:
        return self._board


    def set_board(self, board: list[list] = None) -> None:
        """Set a new board.
        If no board is given, a new one is created with the values provide on the instace creation.
        The pre defined board should have, preferably, the amount of rows and columns provided on the class instace creation; if not, errors may occur.

        Args:
            board (list[list], optional): A pre defined board. Defaults to None.
        """
        if board:  # Pre defined board (for development usage)
            self._board = board
            return
        self.board = super()._create_board(self._rows, self._columns)


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
        if rewrite or self.board[row][column] is None:
            self.board[row][column] = mark
            return True
        return False


    # TODO: CHECK IF THE OBSERER IS WELL IMPLEMENTED
    # TODO: CHECK OTHER METHODS OF IMPLEMENTATION OF THE OBSERVER PATTER
    def add_subscriber(self, subscriber: ISubscriber, event: str, event_args: dict) -> None:
        """Add to the publisher a subscriber linked to an event."""
        if subscriber not in self._subscribers:
            self._subscribers[subscriber] = []
        self._subscribers[subscriber].append({event: event_args})
            

    def remove_subscriber(self, subscriber: ISubscriber, event: str = None) -> None:
        """Remove from the publisher a subscriber's link with a events."""
        for event in self._subscribers[subscriber]:
            if event.keys() == event:
                event.remove(event)
        # Delete subscribers that has no event linked
        if self._subscribers[subscriber] == []:
            del self._subscribers[subscriber]


    def _notify(self, event: str) -> None:
        """Notify all subscribers link to the event."""
        for subscriber, event_list in self._subscribers.items():
            for events in event_list:
                for event_name, event_args in events.items():
                    if event == event_name:
                        subscriber.update(subscriber, event_name, event_args)
                        return
        

def main():
    return


if __name__ == '__main__': 
    main()