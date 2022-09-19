"""User Interface"""

# IMPORTS #
import os  # os.system('cls')

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


# TODO: REFACTOR AND MEKE OPTIONS CLASSES
class SimpleOptionsMenu:
    def __init__(self, title: str, options: list, prompt: str) -> None:
        self.title = title
        self.options = options
        self.prompt = prompt


    def print_options(self) -> None:
        for idx, option in enumerate(self.options):
            print(f'[ {idx + 1} ] >>> {option}')
        

    def get_option(self):
        user_input = int(input(self.prompt))
        return self.options[user_input -1]

    def show(self):
        os.system('cls')
        print(f'{self.title.upper()}')
        print('')
        self.print_options()
        print('')
        return self.get_option()


def main():   
    return


if __name__ == '__main__':
    main()
