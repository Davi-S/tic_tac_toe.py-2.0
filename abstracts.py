"""Abstract Classes"""

# IMPORTS # 
from abc import ABC, abstractmethod

# LOCAL IMPORTS #

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


BOARD_HINT = list[list]


class IBoard(ABC):
    """Is the board of the game. A two dimension array"""

    @property
    @abstractmethod
    def board(self) -> BOARD_HINT: 
        pass

    @abstractmethod
    def place_mark(self) -> bool:
        pass
    
    def _create_board(self, rows: int, columns: int) -> BOARD_HINT:
        """Create a empty two dimention matrix (board)"""
        gridline = [None for _ in range(rows)]
        gridline = [list(gridline) for _ in range(columns)]
        return gridline


class IWinChecker(ABC):
    """Analize wins on the board."""

    @abstractmethod
    def check_win(self) -> bool:
        pass

    @abstractmethod
    def get_win_info(self) -> dict:
        pass


class IPlayer(ABC):
    """A player of the game. Receives a board state and chose where to play."""

    def __init__(self, name: str, mark: str) -> None:
        self.name = name
        self.mark = mark

    @abstractmethod
    def play(self) -> tuple[int, int]:
        pass


# TODO: IMPLEMET ABSTRACT FOR GAME MODES