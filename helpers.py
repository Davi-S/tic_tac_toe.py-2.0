"""Generic useful functions"""

# IMPORTS #

# LOCAL IMPORTS #
from collections import defaultdict

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

def main() -> int:
    return 0
    

if __name__ == "__main__":
    main()