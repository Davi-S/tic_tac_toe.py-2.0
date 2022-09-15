# IMPORTS #
from abc import ABC, abstractmethod, abstractproperty
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

    @property
    @abstractmethod
    def board(self):
        pass

    @abstractmethod
    def place_mark(self):
        pass
    
    def _create_board(self, rows: int, columns: int) -> list[list]:
        """Create a empty 2 dimention matrix (board)"""
        gridline = [None for _ in range(rows)]
        gridline = [list(gridline) for _ in range(columns)]
        return gridline


class IWinChecker(ABC):
    @abstractmethod
    def check_win(self) -> bool:
        pass

    @abstractmethod
    def get_win_info(self):
        pass


class IPlayer(ABC):
    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def mark(self):
        pass
    
    @abstractmethod
    def play(self):
        pass
