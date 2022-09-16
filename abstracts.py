"""Abstract Classes"""

# IMPORTS # 

# LOCAL IMPORTS #
from abc import ABC, abstractmethod

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


class IBoardSubscriber(ABC):
    """The BoardSubscriber interface declares the update_board_state method, used by Publishers to update the board state."""
    
    @abstractmethod
    def update_board_state(self, board_state: list[list]) -> None:
        """Receive update from Publisher."""
        pass


class IPublisher(ABC):
    """The Publisher interface declares a set of methods for managing subscribers."""

    @abstractmethod
    def add_subscriber(self, subscriber: IBoardSubscriber) -> None:
        """Add an subscriber to the publisher."""
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber: IBoardSubscriber) -> None:
        """Remove an subscriber from the publisher."""
        pass

    @abstractmethod
    def notify_subscribers(self) -> None:
        """Notify all subscribers about an event."""
        pass


class IBoard(IPublisher):
    """Is the board of the game. A two dimension array"""

    @property
    @abstractmethod
    def board(self) -> list[list]: 
        pass

    @abstractmethod
    def place_mark(self) -> bool:
        pass
    
    def _create_board(self, rows: int, columns: int) -> list[list]:
        """Create a empty two dimention matrix (board)"""
        gridline = [None for _ in range(rows)]
        gridline = [list(gridline) for _ in range(columns)]
        return gridline


class IWinChecker(IBoardSubscriber):
    """Analize wins on the board."""

    @abstractmethod
    def check_win(self) -> bool:
        pass

    @abstractmethod
    def get_win_info(self) -> dict:
        pass


class IPlayer(IBoardSubscriber):
    """A player of the game. Receives a board state and chose where to play."""

    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark

    @abstractmethod
    def play(self) -> tuple[int, int]:
        pass
