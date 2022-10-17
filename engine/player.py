"""Player concrete classes"""

# standard library imports #
from copy import deepcopy
from itertools import product
from math import inf
from random import randint

# related third party imports #
# local application/library specific imports #
import abstracts
import helpers as hp


# def max_n(state, depht, alfa, beta, maximazing): pass
# def mini_n_max(state, depht, alfa, beta, maximazing): pass

def minimax(game: abstracts.IGame, maximizing: str, depht: int=-1, alpha: int=-inf, beta: int=+inf, actual_player: str=None):
    next_player = list(game.players_score)[0].mark if actual_player == list(game.players_score)[1].mark else list(game.players_score)[1].mark

    marks = [values[0] for values in game.win_checker.win_info().values()]
    if depht == 0 or game.board.is_terminal():
        return {'position': None, 'score': 0}

    elif any(marks):
        if [next_player] in marks:
            return {'position': None, 'score': 1 * (len(game.board.empty_places()) + 1)}
        else:
            return {'position': None, 'score': -1 * (len(game.board.empty_places()) + 1)}

    mval = {'position': None, 'score': -inf} if actual_player == maximizing else {'position': None, 'score': +inf}

    for line, column in product(range(game.board.rows), range(game.board.columns)): # itertools replace nested for loops
        if (line, column) in game.board.empty_places():
            game.board.place_mark(line, column, actual_player)
            val = minimax(game, maximizing, depht-1, alpha, beta, next_player)
            game.board.place_mark(line, column, None, True)  # Undo move
            val['position'] = line, column
            
            if (actual_player == maximizing and val['score'] > mval['score']) or (actual_player != maximizing and val['score'] < mval['score']):
                mval = val
            # if actual_player.mark == maximizing:
            #     mval = val if val['score'] > mval['score'] else mval
            #     # alpha = max(alpha, val['score'])
                
            # elif actual_player.mark != maximizing:
            #     mval = val if val['score'] < mval['score'] else mval
            #     beta = min(beta, val['score'])

            # if beta <= alpha:
            #     break
    return mval



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
        a = minimax(deepcopy(self.game_instance), self.mark, actual_player=self.game_instance.act_player.mark)
        print(a)
        return a['position']

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
