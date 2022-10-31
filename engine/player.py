"""Player concrete classes"""

# standard library imports #
import collections as clct
import itertools as itt
import math as mt
import random as rnd

# related third party imports #
# local application/library specific imports #
import abstracts as ab
import engine.board as bd
import helpers as hp


def evaluate(board_state: bd.BOARD_HINT, mark: str) -> int:
    """Generate a score based in how many groups the given mark is alone

    Args:
        board_state (bd.BOARD_HINT): A board state
        mark (list): the mark to get score

    Returns:
        int: score
    """
    groups = []

    # Add sets of all groups
    groups.extend(set(i) for i in hp.Matrix(board_state).rows())
    groups.extend(set(i) for i in hp.Matrix(board_state).columns())
    groups.extend(set(i) for i in hp.Matrix(board_state).p_diagonals())
    groups.extend(set(i) for i in hp.Matrix(board_state).s_diagonals())

    # Remove Nones
    n_group = []
    for sublist in groups:
        cleaned = [elem for elem in sublist if elem is not None]
        if len(cleaned):
            n_group.append(cleaned)

    # Store all raw score
    df = clct.defaultdict(int)
    for i in n_group:
        if len(i) == 1 and i[0] is not None:
            df[i[0]] += 1

    # Calculate score
    divi = df[mark]
    for key, value in df.items():
        if key != mark:
            divi = divi / value

    return int(divi)


def minimax(player_instance: ab.IPlayer, actual_player: ab.IPlayer, depht: int = -1, alpha: int = -mt.inf, beta: int = +mt.inf) -> list:
    """Only Work for games with two players 

    Args:
        player_instance (abstracts.IPlayer): The players instance. This is the maximizing player
        actual_player (abstracts.IPlayer): The player how holds the turn
        depht (int, optional): Depht of the "three". Negative number to infinit steps. Defaults to -1.
        alpha (int, optional): Do not change. Defaults to -inf.
        beta (int, optional): Do not change. Defaults to +inf.

    Returns:
        list: the best move, score
    """
    # Swap players
    next_player = player_instance.game_instance.players[1] \
        if actual_player.mark == player_instance.game_instance.players[0].mark \
        else player_instance.game_instance.players[0]

    # Chek wins
    if [value for value in player_instance.game_instance.win_checker.win_info().values() if value is not None]:
        # If is maximizing player turn, get a positive multiplier
        multiplier = +1 if next_player.mark == player_instance.mark else -1

        # +1 to avoid multiplications with < 1
        return [None, multiplier * (len(player_instance.game_instance.board.empty_places()) + 1)]

    # Max depht or draw
    elif len(player_instance.game_instance.board.empty_places()) == 0:
        return [None, 0]

    elif depht == 0:
        return [None, evaluate(player_instance.game_instance.board.board, player_instance.mark)]

    # Check if is the maximizing player turn
    maximizing = actual_player.mark == player_instance.mark
    m_eval = [None, -mt.inf] if maximizing else [None, +mt.inf]
    for row, column in itt.product(range(player_instance.game_instance.board.rows), range(player_instance.game_instance.board.columns)):
        if player_instance.game_instance.board.place_mark(row, column, actual_player.mark):
            evaluation = minimax(
                player_instance, next_player, depht - 1, alpha, beta)
            evaluation[0] = row, column
            player_instance.game_instance.board.place_mark(
                row, column, None, True)  # Undo move

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


# # TODO: implement algorithmns
# # mini_n_max(max, min, min)
# def mini_n_max(depht: int, alfa: int, beta: int): pass
# # max_n(max, max, max)
# def max_n(depht: int, alfa: int, beta: int): pass


class HumanPlayer(ab.IPlayer):
    """Handle the input from the user as a player"""

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

        if isinstance(row, int) and isinstance(column, int):  # remove extra from input
            row, column = row-1, column-1
        return row, column


class EasyPlayer(ab.IPlayer):
    """Play on a random place of the board"""

    def __init__(self, name: str, mark: str) -> None:
        super().__init__(name, mark)

    def play(self) -> tuple[int, int]:
        """Choose a random empty coordinate from the board

        Returns:
            tuple[int, int]: The coordinate chosen
        """
        possible_plays = self.game_instance.board.empty_places()
        return possible_plays[rnd.randint(0, len(possible_plays) - 1)]


class MediumPlayer(ab.IPlayer):
    def play(self) -> tuple[int, int]:
        return minimax(self, self, 2)[0]


class HardPlayer(ab.IPlayer):
    def play(self) -> tuple[int, int]:
        return minimax(self, self, 5)[0]


class ImpossiblePlayer(ab.IPlayer):
    def play(self) -> tuple[int, int]:
        return minimax(self, self, -1)[0]


class AdaptativePlayer(ab.IPlayer): # sourcery skip: assign-if-exp, reintroduce-else
    def play(self, depht: int = -1) -> tuple[int, int]:
        if depht <= 0:
            possible_plays = self.game_instance.board.empty_places()
            return possible_plays[rnd.randint(0, len(possible_plays) - 1)]

        return minimax(self, self, depht)[0]


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
