"""Generic useful functions"""

# standard library imports #
import itertools
from collections import defaultdict
from random import randrange

# related third party imports #
from names import get_first_name

# local application/library specific imports #
import engine.board as bd


def longest_consecutive_occourence(iterable, item) -> list:
    """Count the longest consecutive occourence of the given item on the given iterable

    Args:
        iterable (iterable): the iterable to search on
        key (value): the key being searched

    Returns:
        list: occourence_len, (start_index, end_index)
    """
    item_list = None
    longest_len = None
    for i, j in itertools.groupby(iterable):
        if i == item:
            item_list = list(j)
            longest_len = len(item_list)

    indexes = [(i, i + len(item_list)) for i in range(len(iterable))
               if iterable[i: i + len(item_list)] == item_list]

    return [longest_len, indexes[0]]


# TODO: make this return all the coordinates of the group
class Matrix:
    """Get information on a matrix"""
    
    def __init__(self, matrix: bd.BOARD_HINT) -> None:
        self.matrix = matrix
        
    def _get_groups(self, group_function):
        grouping = defaultdict(list)
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                grouping[group_function(x, y)].append(self.matrix[x][y])
        return list(map(grouping.get, sorted(grouping)))

    def rows(self):
        return self._get_groups(lambda x, y: x)

    def row_coords(self, index: int):
        return [(index, i) for i in range(len(self.rows()[index]))]
    
    def columns(self):
        return self._get_groups(lambda x, y: y)
        
    def column_coords(self, index: int):
        return [(i, index) for i in range(len(self.columns()[index]))]

    def s_diagonals(self):
        return self._get_groups(lambda x, y: x + y)
    
    def s_diagonal_coords(self, index: int):
        return two_digit_sum(index)

    def p_diagonals(self):
        return self._get_groups(lambda x, y: x - y)
    
    def p_diagonal_coords(self, index: int):
        coords = two_digit_sum(index)
        coords = self.valid_coords(coords)
        return [(i[0], len(self.rows()[i[0]]) - i[1] - 1) for i in coords]
    
    def valid_coords(self, coords: list):
        return[i for i in coords if (i[0] <= len(self.columns()) - 1) and (i[1] <= len(self.rows()) - 1)]
         

def is_char(char) -> bool:
    """Check if the given object is a single char

    Args:
        char (any type): What will be checked

    Returns:
        bool: Return True if the given object is a single char. Else, False
    """
    char = str(char)
    return char.isalpha() and len(char) == 1


def random_char(exclude: list) -> str:
    """Return a letter of the alphabet

    Args:
        exclude (list): Letters the will not be chossen

    Returns:
        str: The letter
    """
    while True:
        char = ''.join(chr(randrange(97, 122)))
        if char not in exclude:
            break
    return char


def random_name(exclude: list) -> str:
    """Return a random person first name

    Args:
        exclude (list): Namer the will not be chossen

    Returns:
        str: The name
    """
    while True:
        name = get_first_name()
        if name not in exclude:
            break
    return name


def get_int_max(prompt: str, n_range: range) -> int | str:
    """Get a int from the user in the given range.
    If the user fails to provide a valid input a str contain the error message is return.
    Otherwise, return the int

    Args:
        prompt (str): The prompt shown on the scree
        n_range (range): The valid range for the input

    Returns:
        int | str: The int provided from the user or a error message
    """
    user_input = input(prompt)
    if not user_input.isdigit():
        return 'Choose a integer number'

    user_input = int(user_input)
    if user_input not in n_range:
        return 'Choose a number in the options range'

    return user_input


def print_formated_board(board: bd.BOARD_HINT) -> None:
    """Print a user frendly board on the terminal

    Args:
        board (BOARD_HINT): A board
    """
    for line_idx, line in enumerate(board):
        # Formatting the list
        print('\n', str(line).replace('[', '')
                             .replace(']', '')
                             .replace(',', ' |')
                             .replace("'", '')
                             .replace('None', ' '))
        if line_idx < len(board) - 1:
            for count, _ in enumerate(line, start=1):
                print('---', end='')
                if count < len(line):
                    print('|', end='')

def two_digit_sum(res: int) -> list:
    """Get all two digits that when sum, results in "res"

    Args:
        res (int): The final sum

    Returns:
        list: list of tuples
    """
    a = list(range(res +1))
    b = list(range(res, -1, -1))
    return list(zip(a, b))

def main() -> int:
    b = [['x', 'x', None], [None, 'o', None], ['x', None, 'o']]

    return 0


if __name__ == "__main__":
    main()
