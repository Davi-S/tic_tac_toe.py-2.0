"""Terminal user interface"""

# IMPORTS #
from os import system
from time import sleep

# LOCAL IMPORTS #
from engine.board import BOARD_HINT


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


def print_formated_board(board: BOARD_HINT) -> None:
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


def print_options(options: dict) -> None:
    """Print a user frendly list of options

    Args:
        options (dict): keys: option name. value: option description
    """
    for idx, values in enumerate(options.items()):
        if values[1]:
            print(f"[ {idx+1} ] >>> {values[0]} --> {values[1]}")
        else:
            print(f"[ {idx+1} ] >>> {values[0]}")
    return


def print_title(title: str):
    print(len(title) * '-')
    print(title.upper())
    print(len(title) * '-')


def options_menu(title: str, options: dict, prompt: str = 'Choose an option: ') -> str:
    """A menu for the user choose a option from

    Args:
        title (str): The menu title
        options (dict): The menu options
        prompt (str, optional): Prompt shown for the user to type. Defaults to 'Choose an option: '.

    Returns:
        str: The name of the option choosen
    """
    while True:
        system('cls')
        print_title(title)
        print_options(options)
        print()
        option = get_int_max(prompt, range(1, len(options) + 1))
        # int return successfully
        if isinstance(option, int):
            break
        # error message receive
        print(option)
        sleep(2)
    return list(options)[option - 1]


def type_menu(title: str, prompt: str) -> str:
    """A open menu for the user to type in

    Args:
        title (str): The menu title
        prompt (str): Prompt shown for the user to type

    Returns:
        str: What the user typed
    """
    system('cls')
    print_title(title)
    return input(prompt)