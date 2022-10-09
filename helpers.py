"""Generic useful functions"""

# IMPORTS #
from collections import defaultdict
from random import randrange
from names import get_first_name

# LOCAL IMPORTS #
import abstracts 


def longest_consecutive_occourence(iterable, item) -> int:
    """Count the longest consecutive occourence of the given item on the given iterable

    Args:
        iterable (iterable): the iterable to search on
        key (value): the key being searched

    Returns:
        int: longest consecutive occourence of the given item
    """
    if item not in iterable:
        return 0
    longest = 0
    actual = 0
    previous = None
    for i in iterable:
        if i == item and previous == item:
            actual += 1
            if actual >= longest:
                longest = actual
            continue
        actual = 0
        previous = i
    # "+ 1" because the counters start at 0 and if the code reach here, the number is on the list and there is at least one occourence of it
    return longest + 1


class Matrix:
    """Get groups of a matrix. (row, columns and diagonals)"""
    @staticmethod
    def _get_groups(matrix, group_function):
        grouping = defaultdict(list)
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                grouping[group_function(x, y)].append(matrix[x][y])
        return list(map(grouping.get, sorted(grouping)))

    @classmethod
    def rows(cls, matrix):
        return cls._get_groups(matrix, lambda x, y: x)

    @classmethod
    def columns(cls, matrix):
        return cls._get_groups(matrix, lambda x, y: y)

    @classmethod
    def p_diagonals(cls, matrix):
        return cls._get_groups(matrix, lambda x, y: x + y)

    @classmethod
    def s_diagonals(cls, matrix):
        return cls._get_groups(matrix, lambda x, y: x - y)


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


def print_formated_board(board: abstracts.BOARD_HINT) -> None:
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


def main() -> int:
    return 0


if __name__ == "__main__":
    main()
