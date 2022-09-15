"""Abstract Classes"""

# IMPORTS # 

# LOCAL IMPORTS #
from abc import ABC, abstractmethod, abstractproperty

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


class IBoard(ABC):
    """It is and can manipulate the board"""

    @property
    @abstractmethod
    def board(self) -> list[list]: 
        pass

    @abstractmethod
    def place_mark(self) -> bool:
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
