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
    if actual_player.mark == list(player_instance.game_instance.players_score.keys())[0].mark:
        next_player = list(
            player_instance.game_instance.players_score.keys())[1]
    else:
        next_player = list(
            player_instance.game_instance.players_score.keys())[0]

    if [player[0] for player in player_instance.game_instance.win_checker.win_info().values() if player[0] is not None]:
        if next_player.mark == player_instance.mark:
            return [None, 1 * (len(player_instance.game_instance.board.empty_places()) + 1)]
        else:
            return [None, -1 * (len(player_instance.game_instance.board.empty_places()) + 1)]

    elif depht == 0 or len(player_instance.game_instance.board.empty_places()) == 0:
        return [None, 0]

    if actual_player.mark == player_instance.mark:  # maximizing_player
        max_eval = [None, -inf]
        for row, column in product(range(player_instance.game_instance.board.rows), range(player_instance.game_instance.board.columns)):
            if player_instance.game_instance.board.place_mark(row, column, actual_player.mark):
                evaluation = minimax(
                    player_instance, next_player, depht - 1, alpha, beta)
                player_instance.game_instance.board.place_mark(
                    row, column, None, True)  # undo move
                evaluation[0] = row, column

                if evaluation[1] > max_eval[1]:
                    max_eval = evaluation

                if evaluation[1] > alpha:
                    alpha = evaluation[1]

                if beta <= alpha:
                    break
        return max_eval

    else:
        min_eval = [None, +inf]
        for row, column in product(range(player_instance.game_instance.board.rows), range(player_instance.game_instance.board.columns)):
            if player_instance.game_instance.board.place_mark(row, column, actual_player.mark):
                evaluation = minimax(
                    player_instance, next_player, depht - 1, alpha, beta)
                player_instance.game_instance.board.place_mark(
                    row, column, None, True)  # undo move
                evaluation[0] = row, column

                if evaluation[1] < min_eval[1]:
                    min_eval = evaluation

                if evaluation[1] < beta:
                    beta = evaluation[1]

                if beta <= alpha:
                    break
        return min_eval
    
    
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

    def play_MM(self):
        return minimax(self, self)[0]

    def play_MnM(self):
        return mini_n_max()

    def play_Mn(self):
        return max_n()


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
