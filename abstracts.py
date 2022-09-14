# IMPORTS #
from abc import ABC, abstractmethod

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


class ISubscriber(ABC):
    """The Observer interface declares the update method, used by Publisher."""

    @abstractmethod
    def update(self, event) -> None:
        """Receive update from Publisher."""
        pass


class IPublisher(ABC):
    """The Subject interface declares a set of methods for managing subscribers."""

    @abstractmethod
    def add_subscriber(self, subscriber, events) -> None:
        """Add an subscriber to the publisher."""
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber, events) -> None:
        """Remove an subscriber from the publisher."""
        pass

    @abstractmethod
    def notify(self, events) -> None:
        """Notify all subscribers about an event."""
        pass


class IBoard(ABC):
    """It is and can manipulate the board"""

    @abstractmethod
    def set_board(self):
        pass

    @abstractmethod
    def place_mark(self):
        pass

    def _create_board(self, rows: int, columns: int) -> list[list]:
        """Create a empty matrix"""
        gridline = [None for _ in range(rows)]
        gridline = [list(gridline) for _ in range(columns)]
        return gridline


class IWinChecker(ABC):
    def set_board_state(self, board_state: list[list]) -> None:
        self.board_state = board_state
        
    @abstractmethod
    def check_win(self) -> bool:
        pass

    @abstractmethod
    def get_win_info(self):
        pass


class IPlayer(ABC):
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
