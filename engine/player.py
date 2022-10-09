"""Player concrete classes"""

# IMPORTS #
from random import randint

# LOCAL IMPORTS #
import abstracts
import helpers as hp 


class HumanPlayer(abstracts.IPlayer):
    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, mark)

    def play(self) -> tuple[int, int]:
        """Get row and column from user input

        Returns:
            tuple[int, int]: row and column
        """
        # changing ranges to better user friendly
        row = hp.get_int_max('ROW: ',
                             range(1, len(self.game_instance.board.board) + 2))
        
        column = hp.get_int_max('COLUMN: ',
                                range(1, len(self.game_instance.board.board) + 2))
        
        if isinstance(row, int) and isinstance(column, int):  # remove extra input
            row, column = row-1, column-1
        return row, column


class EasyPlayer(abstracts.IPlayer):
    """Play on a random place of the board"""

    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, mark)

    def play(self) -> tuple[int, int]:
        """Choose a random empty coordinate from the board

        Returns:
            tuple[int, int]: The coordinate chosen
        """
        possible_plays = self.game_instance.board.empty_places()
        return possible_plays[randint(0, len(possible_plays) - 1)]


# TODO: implement classes
# TODO: implement MinMax algorithmn
# MinMax(max, min, min)
# MinMax(max, max, max)
class MediumPlayer(EasyPlayer):
    """Always block oponent wins if possible"""

    def play(self):
        pass


class HardPlayer(MediumPlayer):
    """Always win if possible"""

    def play(self):
        pass


class ImpossiblePlayer(MediumPlayer):
    """Never looses"""

    def play(self):
        pass


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
