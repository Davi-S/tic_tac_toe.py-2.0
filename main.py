"""Main file. Meant do be run"""

# IMPORTS #
from os import system
from itertools import cycle

# LOCAL IMPORTS #
from engine.player import EasyPlayer, HumanPlayer
from engine.win_check import ClassicWinChecker
from engine.board import Board2D
from helpers import type_menu, options_menu, print_formated_board

SLEEP_TIME = 2

# TODO: make better game loop
def play_classic(players_init: dict):
    while True:
        # pre game
        board = Board2D(3, 3)
        players = players_init
        # set board instance to players
        for player in players:
            player.set_board(board)

        players_cycle = cycle(players)  # infinity iterable

        while True:  # game loop
            system('cls')
            print_formated_board(board.board)
            act_player = next(players_cycle)
            row, column = act_player.play()
            board.place_mark(row, column, act_player.mark)
            if ClassicWinChecker(board.board).check_win():
                input('arst')
                break


# TODO: make and set others dificults
def pick_dificulty():
    dificulty_menu = options_menu('dificulty', {'easy': '', 'medium': '', 'hard': '', 'impossible': ''})
    dificulty = None
    # TODO: add dificultys
    match dificulty_menu:
        case 'easy':
            dificulty = EasyPlayer
        case 'medium':
            pass
        case 'hard':
            pass
        case 'impossible':
            pass
    return dificulty


def add_players(amount, title: str):
    players = []
    for i in range(amount):
        name = type_menu(title.format(i + 1), 'nickname: ')
        mark = type_menu(title.format(i + 1), 'mark: ')
        players.append(HumanPlayer(name, mark))
    return players


def classic_configuration():
    while True:
        players_menu = options_menu('opponent', {'IA': '', 'local': '', 'back': ''})
        match players_menu:
            case 'IA':
                ia_dificulty = pick_dificulty()
                players = {player: 0 for player in add_players(1, f'set your profile')}
                # TODO: add name and mark generator
                players[ia_dificulty(name='randon', mark='a')] = 0
            case 'local':
                players = {player: 0 for player in add_players(2, 'set player {} profile')}
            case 'back':
                return

        start_menu = options_menu('start', {'start': '', 'change settings': ''})
        match start_menu:
            case 'start':
                play_classic(players)
            case 'change settings':
                continue
            case 'back':
                return
    

# TODO: make and add other game modes
def game_modes():
    while True:
        game_mode_menu_options = {'classic': '', 'teams': '', 'other': '', 'back': ''}
        game_mode_menu = options_menu('game modes', game_mode_menu_options)
        match game_mode_menu:
            case 'classic':
                classic_configuration()
            case 'teams':
                pass
            case 'other':
                pass
            case 'back':
                return


# TODO: make other options
def main_menu():
    while True:
        main_menu_options = {'play': '', 'options': '', 'quit': ''}
        main_menu = options_menu('main menu', main_menu_options)
        match main_menu:
            case 'play':
                game_modes()
            case 'options':
                pass
            case 'quit':
                return


def main() -> int:
    system('cls')
    main_menu()
    return 0


if __name__ == '__main__':
    main()
