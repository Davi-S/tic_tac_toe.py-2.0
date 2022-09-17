"""User Interface"""

# IMPORTS #

# LOCAL IMPORTS #

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))



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


def print_options(options: dict[int, str]) -> None:
    for option_number, option_name in options.items():
        print(f'[ {option_number} ] >>> {option_name}')



def main():
    options = {1: 'opt1', 2: 'opt2', 3: 'opt3'}
    
    return


if __name__ == '__main__':
    main()
