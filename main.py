"""Main file. Meant do be run"""

# First of all, setup logging configuration. This is only needed on the main file. Will affect all other log instances in other files
from time import sleep
from os import system
import logging
import logging.config
from logs.logging_configuration import CONFIG_DICT, create_file_handler
logging.config.dictConfig(CONFIG_DICT)
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))

# IMPORTS #

# LOCAL IMPORTS #
SLEEP_TIME = 2


def get_option(max: int, prompt: str):
    user_input = input(prompt)
    if not user_input.isdigit():
        print('Choose a integer number')
        sleep(SLEEP_TIME)
        return None

    user_input = int(user_input)
    if not 0 <= user_input < max:
        print('Choose a number in the options range')
        sleep(SLEEP_TIME)
        return None

    return user_input


def print_options(options: dict):
    for idx, values in enumerate(options.items()):
        print(f"[ {idx} ] >>> {values[0]} --> {values[1]}")
    return


def menu(title: str, options: dict, prompt: str = 'Choose an option: '):
    option = None
    while not isinstance(option, int):
        system('cls')
        print(len(title) * '-')
        print(title.upper())
        print(len(title) * '-')
        print_options(options)
        option = get_option(len(options), prompt)
    return list(options)[option]


# TODO: make game mode configurations

def game_modes():
    while True:
        game_mode_menu_options = {'classic': '', 'teams': '', 'other': '', 'back': ''}
        game_mode_menu = menu('game modes', game_mode_menu_options)
        match game_mode_menu:
            case 'classic':
                pass
            case 'teams':
                pass
            case 'other':
                pass
            case 'back':
                return


def main_menu():
    while True:
        main_menu_options = {'play': '', 'options': '', 'quit': ''}
        main_menu = menu('main menu', main_menu_options)
        match main_menu:
            case 'play':
                game_modes()
            case 'option':
                print('option')
            case 'quit':
                print('quit')


def main() -> int:
    system('cls')
    main_menu()
    return 0


if __name__ == '__main__':
    main()
