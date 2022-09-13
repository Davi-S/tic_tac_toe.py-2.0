# IMPORTS #
from collections import defaultdict

from logs.logging_configuration import create_file_handler
import logging

# Get the file logger and its handler
log = logging.getLogger(__name__)
log.addHandler(create_file_handler(__name__))


def print_formated_board(board: list[list]):
    """Print a user frendly board on the terminal"""
    for line_idx, line in enumerate(board):
        # Formatting the list
        print('\n', str(line).replace('[', '')
                             .replace(']', '')
                             .replace(',', ' |')
                             .replace("'", ''))
        if line_idx < len(board) -1:
            for count, _ in enumerate(line, start=1):
                print('---', end='')
                if count < len(line):
                    print('|', end='')


# TODO: MAKE A COMMAND LINE INTERFACE SO THE USER CAN PLAY THE GAME