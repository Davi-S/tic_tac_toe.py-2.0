"""Main file. Meant do be run"""

# First of all, setup logging configuration. This is only needed on the main file. Will affect all other log instances in other files
import logging
import logging.config
from logs.logging_configuration import CONFIG_DICT, create_file_handler
logging.config.dictConfig(CONFIG_DICT)
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))

# IMPORTS #
from helpers import type_menu, options_menu
from os import system

# LOCAL IMPORTS #
from engine.player import EasyPlayer, HumanPlayer
from engine.board import Board2D



SLEEP_TIME = 2


def play_classic(players: list):
    score = 0
    


def classic_configuration():
    while True:
        players = {'player1': None, 'Player2': None}
        players_menu = options_menu('opponent', {'IA': '', 'local': '', 'back': ''})
        match players_menu:
            # set players name and mark
            case 'IA':
                name = type_menu('Your nickname: ')
                mark = type_menu('Your mark: ')
                players['player1'] = HumanPlayer(name, mark)
                
                # TODO: set dificulty and IA
            case 'local':
                pass
            case 'back':
                return
        
        start_menu = options_menu('start', {'start': '', 'change settings': ''})
        match start_menu:
            # set players name and mark
            case 'start':
                play_classic()
            case 'change settings':
                continue
            case 'back':
                return
    


def game_modes():
    while True:
        game_mode_menu_options = {'classic': '', 'teams': '', 'other': '', 'back': ''}
        game_mode_menu = options_menu('game modes', game_mode_menu_options)
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
        main_menu = options_menu('main menu', main_menu_options)
        match main_menu:
            case 'play':
                game_modes()
            case 'options':
                print('options')
            case 'quit':
                print('quit')


def main() -> int:
    system('cls')
    main_menu()
    return 0


if __name__ == '__main__':
    main()
