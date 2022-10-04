"""Generic useful functions"""

# IMPORTS #
from time import sleep
from os import system
from collections import defaultdict

# LOCAL IMPORTS #

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


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
    def p_diagonal(cls, matrix):
        return cls._get_groups(matrix, lambda x, y: x + y)

    @classmethod
    def s_diagonal(cls, matrix):
        return cls._get_groups(matrix, lambda x, y: x - y)


def is_char(char: str) -> bool:
    """Check if the given str is a single char"""
    return False if type(char) != str else 0 > len(char) > 1



def print_formated_board(board: list[list]) -> None:
    """Print a user frendly board on the terminal"""
    for line_idx, line in enumerate(board):
        # Formatting the list
        print('\n', str(line).replace('[', '')
                             .replace(']', '')
                             .replace(',', ' |')
                             .replace("'", '')
                             .replace('None', ' '))
        if line_idx < len(board) -1:
            for count, _ in enumerate(line, start=1):
                print('---', end='')
                if count < len(line):
                    print('|', end='')


def get_int_max(prompt: str, max: int) -> int:
    user_input = input(prompt)
    if not user_input.isdigit():
        print('Choose a integer number')
        sleep(2)
        return None

    user_input = int(user_input)
    if not 0 <= user_input < max:
        print('Choose a number in the options range')
        sleep(2)
        return None

    return user_input


def print_options(options: dict) -> None:
    for idx, values in enumerate(options.items()):
        print(f"[ {idx} ] >>> {values[0]} --> {values[1]}")
    return


def options_menu(title: str, options: dict, prompt: str = 'Choose an option: ') -> str:
    option = None
    while not isinstance(option, int):
        system('cls')
        print(len(title) * '-')
        print(title.upper())
        print(len(title) * '-')
        print_options(options)
        option = get_int_max(prompt, len(options))
    return list(options)[option]
 

def type_menu(title: str, prompt: str) -> str:
    system('cls')
    print(len(title) * '-')
    print(title.upper())
    print(len(title) * '-')
    return input(prompt)


def main() -> int:
    return 0
    

if __name__ == "__main__":
    main()