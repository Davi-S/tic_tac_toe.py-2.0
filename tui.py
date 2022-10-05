"""Terminal user interface"""

# IMPORTS #
from os import system
from time import sleep

# LOCAL IMPORTS #


def get_int_max(prompt: str, minimum: int, maximum: int) -> int:
    user_input = input(prompt)
    if not user_input.isdigit():
        print('Choose a integer number')
        sleep(2)
        return

    user_input = int(user_input)
    if not minimum <= user_input <= maximum:
        print('Choose a number in the options range')
        sleep(2)
        return

    return user_input


def print_formated_board(board: list[list]) -> None:
    """Print a user frendly board on the terminal"""
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


def print_options(options: dict) -> None:
    for idx, values in enumerate(options.items()):
        if values[1]:
            print(f"[ {idx+1} ] >>> {values[0]} --> {values[1]}")
        else:
            print(f"[ {idx+1} ] >>> {values[0]}")
    return


def options_menu(title: str, options: dict, prompt: str = 'Choose an option: ') -> str:
    while True:
        system('cls')
        print(len(title) * '-')
        print(title.upper())
        print(len(title) * '-')
        print_options(options)
        print()
        option = get_int_max(prompt, 1, len(options))
        if isinstance(option, int):
            break
    return list(options)[option - 1]


def type_menu(title: str, prompt: str) -> str:
    system('cls')
    print(len(title) * '-')
    print(title.upper())
    print(len(title) * '-')
    return input(prompt)
