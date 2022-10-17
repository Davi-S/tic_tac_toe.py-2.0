"""Player concrete classes"""

# standard library imports #
from itertools import product
from math import inf
from random import randint

# related third party imports #
# local application/library specific imports #
import abstracts
import helpers as hp


def minimax(player_instance: abstracts.IPlayer, actual_player: abstracts.IPlayer, depht=-1, alpha=-inf, beta=+inf):
    # Swap players
    next_player = player_instance.game_instance.player_list[1] \
        if actual_player.mark == player_instance.game_instance.player_list[0].mark \
        else player_instance.game_instance.player_list[0]

    # Chek wins
    if [player[0] for player in player_instance.game_instance.win_checker.win_info().values() if player[0] is not None]:
        # If is maximizing player turn, get a positive multiplier
        multiplier = +1 if next_player.mark == player_instance.mark else -1
        return [None, multiplier * (len(player_instance.game_instance.board.empty_places()) + 1)]

    # Max depht or draw
    elif depht == 0 or len(player_instance.game_instance.board.empty_places()) == 0:  
        return [None, 0]

    maximizing = actual_player.mark == player_instance.mark  # Check if is the maximizing player turn
    m_eval = [None, -inf] if maximizing else [None, +inf]
    for row, column in product(range(player_instance.game_instance.board.rows), range(player_instance.game_instance.board.columns)):
        if player_instance.game_instance.board.place_mark(row, column, actual_player.mark):
            evaluation = minimax(player_instance, next_player, depht - 1, alpha, beta)
            evaluation[0] = row, column
            player_instance.game_instance.board.place_mark(row, column, None, True)  # Undo move

            # Get best score for the actual player
            if maximizing and evaluation[1] > m_eval[1] or not maximizing and evaluation[1] < m_eval[1]:
                m_eval = evaluation

    	    # Alpha-Beta pruning
            if maximizing:
                if evaluation[1] > alpha:
                    alpha = evaluation[1]
            elif evaluation[1] < beta:
                beta = evaluation[1]

            if beta <= alpha:
                break

    return m_eval    
    
    
# TODO: implement algorithmns:
# MinMax(max, min, min)
# MinMax(max, max, max)
def mini_n_max(depht, alfa, beta): pass
def max_n(depht, alfa, beta): pass


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


class MediumPlayer(EasyPlayer):
    """Always block oponent wins if possible"""

    def play(self):
        # try:
        #     play
        # except (there is nowhere to block):
        #     super().play
        pass


class HardPlayer(MediumPlayer):
    """Always win if possible"""

    def play(self):
        # try:
        #     play
        # except (there is nowhere to win):
        #     super().play
        pass


class ImpossiblePlayer(abstracts.IPlayer):
    """Never looses"""

    def play(self):
        a = minimax(self, self)
        return minimax(self, self)[0]

    # def play_MnM(self):
    #     return mini_n_max()

    # def play_Mn(self):
    #     return max_n()


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
