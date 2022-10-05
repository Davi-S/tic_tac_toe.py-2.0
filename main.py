"""Main file. Meant do be run"""

# IMPORTS #
from os import system
from itertools import cycle
from time import sleep

# LOCAL IMPORTS #
from engine.player import EasyPlayer, HumanPlayer, IPlayer
from engine.win_check import ClassicWinChecker
from engine.board import Board2D
from tui import type_menu, options_menu, print_formated_board
from helpers import random_char, random_name, is_char


# players cannot have same name or mark
PLAYERS: list[IPlayer] = []


# TODO: make better game loop -> more user frendly
# FIXME: fix game end
def play_classic():
    # pre game
    while True:
        board = Board2D(3, 3)
        players = {player: 0 for player in PLAYERS}  # player and score

        # set board instance to players
        for player in players:
            player.set_board(board)

        players_cycle = cycle(players)  # infinity iterable

        # game loop
        while True:  
            system('cls')
            print_formated_board(board.board)
            act_player = next(players_cycle)
            print(f'{act_player.name} turn')
            row, column = act_player.play()
            board.place_mark(row, column, act_player.mark)
            sleep(1)
            if ClassicWinChecker(board.board).check_win():
                input('arst')
                break


# TODO: make others dificults
def pick_dificulty():
    dificulty_menu = options_menu('ia dificulty', {'Easy': '', 'Medium': '', 'Hard': '', 'Impossible': ''})
    # TODO: add dificultys
    match dificulty_menu:
        case 'Easy':
            dificulty = EasyPlayer
        case 'Medium':
            dificulty = None
        case 'Hard':
            dificulty = None
        case 'Impossible':
            dificulty = None
    return dificulty


def get_user_players(amount: int) -> None:
    """Add players to the global players variable by user input

    Args:
        amount (int): amount of players to add
    """
    count = 1
    while count <= amount:
        name = type_menu(f'Set {count}º player profile', 'Nickname: ')
        mark = type_menu(f'Set {count}º player profile', 'Mark: ')

        if not is_char(mark):
            print('The mark must be one letter')
            sleep(2)
            continue
        if mark in [player.mark for player in PLAYERS]:
            print('This mark is alread in use')
            sleep(2)
            continue
        if name in [player.name for player in PLAYERS]:
            print('This name is alread in use')
            sleep(2)
            continue
     
        PLAYERS.append(HumanPlayer(name, mark))
        count += 1


def classic_configuration():
    while True:
        players_menu = options_menu('opponent', {'IA': 'Play against the computer. Custom dificulty',
                                    'Local': 'Local match up',
                                    'Back': ''})
        match players_menu:
            case 'IA':
                ia_dificulty = pick_dificulty()

                # player profile 
                get_user_players(1)

                # IA profile
                PLAYERS.append(ia_dificulty(name=random_name([player.name for player in PLAYERS]),
                                            mark=random_char([player.mark for player in PLAYERS])))
            case 'Local':
                # no IA profile
                get_user_players(2)
            case 'Back':
                return

        start_menu = options_menu('start classic game', {'Start': '', 'Change settings': '', 'Back': ''})
        match start_menu:
            case 'Start':
                play_classic()
            case 'Change settings':
                continue
            case 'Back':
                return
    

# TODO: make and add more game modes
def game_modes():
    while True:
        game_mode_menu_options = {'Classic': 'Two players against each other. 3x3 board. Classic win rules',
                                  'Teams': 'Up to five players on each team (two teams). board up to 12x12. Custom sequence win',
                                  'Back': ''}
        game_mode_menu = options_menu('game modes', game_mode_menu_options)
        match game_mode_menu:
            case 'Classic':
                classic_configuration()
            case 'Teams':
                pass
            case 'Back':
                return


# TODO: make Options option
def main_menu():
    while True:
        main_menu_options = {'Play': '', 'Options': '', 'Quit': ''}
        main_menu = options_menu('main menu', main_menu_options)
        match main_menu:
            case 'Play':
                game_modes()
            case 'Options':
                pass
            case 'Quit':
                return


def main() -> int:
    system('cls')
    main_menu()
    return 0


if __name__ == '__main__':
    main()
