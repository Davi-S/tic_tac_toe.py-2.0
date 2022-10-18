"""Player concrete classes"""

# standard library imports #
from collections import defaultdict
from itertools import product
from math import inf
from random import randint

# related third party imports #
# local application/library specific imports #
import abstracts
import helpers as hp


def evaluate(board_state, mark):
    groups = []

    groups.extend(set(i) for i in hp.Matrix(board_state).rows())
    groups.extend(set(i) for i in hp.Matrix(board_state).columns())
    groups.extend(set(i) for i in hp.Matrix(board_state).p_diagonals())
    groups.extend(set(i) for i in hp.Matrix(board_state).s_diagonals())

    n_group = []
    for sublist in groups:
        cleaned = [elem for elem in sublist if elem is not None]
        if len(cleaned):
            n_group.append(cleaned)

    df = defaultdict(int)
    for i in n_group:
        if len(i) == 1 and i[0] is not None:
            df[i[0]] += 1

    divi = df[mark]
    for key, value in df.items():
        if key != mark:
            divi = divi / value

    return int(divi)


def minimax(player_instance: abstracts.IPlayer, actual_player: abstracts.IPlayer, depht=-1, alpha=-inf, beta=+inf):
    # Swap players
    next_player = player_instance.game_instance.player_list[1] \
        if actual_player.mark == player_instance.game_instance.player_list[0].mark \
        else player_instance.game_instance.player_list[0]

    # Chek wins
    if [value for value in player_instance.game_instance.win_checker.win_info().values() if value is not None]:
        # If is maximizing player turn, get a positive multiplier
        multiplier = +1 if next_player.mark == player_instance.mark else -1
        return [None, multiplier * (len(player_instance.game_instance.board.empty_places()) + 1)]

    # Max depht or draw
    elif len(player_instance.game_instance.board.empty_places()) == 0:
        return [None, 0]

    elif depht == 0:
        return [None, evaluate(player_instance.game_instance.board.board, player_instance.mark)]

    # Check if is the maximizing player turn
    maximizing = actual_player.mark == player_instance.mark
    m_eval = [None, -inf] if maximizing else [None, +inf]
    for row, column in product(range(player_instance.game_instance.board.rows), range(player_instance.game_instance.board.columns)):
        if player_instance.game_instance.board.place_mark(row, column, actual_player.mark):
            evaluation = minimax(
                player_instance, next_player, depht - 1, alpha, beta)
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
# mini_n_max(max, min, min)
def mini_n_max(depht, alfa, beta): pass
# max_n(max, max, max)
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
        return minimax(self, self, 2)[0]


class HardPlayer(MediumPlayer):
    """Always win if possible"""

    def play(self):
        return minimax(self, self, 5)[0]


class ImpossiblePlayer(HardPlayer):
    """Never looses"""

    def play(self):
        return minimax(self, self)[0]


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
