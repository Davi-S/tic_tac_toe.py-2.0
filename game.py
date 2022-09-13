# IMPORTS #
from abstracts import Board, Player, WinChecker
import helpers

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


# TODO: IMPLEMENT THE TICTACTOEGAME CLASS
# TODO: EVERY TIME THAT THE BOARD CHANGES, THE GAME SHOULD UPDATE THE CLASSES REGISTERED ON THE OBSERVER FOR THIS
class TicTacToeGame:
    """
    manage the game
    define rules
    receive the players
    tell players the rules
    create the board as needed
    manage turns
    look at the board and show it to the players
    collects the coordinates of the player who is on turn
    tell the board where to place a mark
    verify wins using the win check (based on what is sees on the board, the players info mark, and rules)
    count score
    """
    def __init__(self, board_class: Board, win_checker_class: WinChecker) -> None:
        self._board = board_class
        self._win_checker = win_checker_class
        self._players = []


    def add_player(self, name: str, mark: str, player: Player) -> bool:
        """Add a player to the game

        Args:
            name (str): Player name. Shown on GUI
            mark (str): The player mark. What will be placed on the board
            player (Player): The Player Class (responsible for sending the coordinates of the moves to the game)
        """
        if not helpers.is_char(mark):
            return False
        if not self._available_player_info(name, mark):
            return False
        self._players.append({'name': name, 'mark': mark, 'player': player})
        return True


    def _available_player_info(self, name: str, mark: str) -> bool: # sourcery skip: use-any, use-next
        """Check if a player exists with the same name or mark

        Args:
            name (str): player name
            mark (str): player mark

        Returns:
            bool: False if a player with the same info exists; Otherwise, True
        """
        for player in self._players:
            if (player['name'] == name) or (player['mark'] == mark):
                return False
        return True

    
def main():  
    return


if __name__ == '__main__': 
    main()