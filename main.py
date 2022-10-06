"""Main file. Meant do be run"""

# IMPORTS #
from os import system
from itertools import cycle
from time import sleep

# LOCAL IMPORTS #
from engine.player import EasyPlayer, HumanPlayer, IPlayer, MediumPlayer, HardPlayer, ImpossiblePlayer
from engine.win_check import ClassicWinChecker
from engine.board import Board2D
from tui import type_menu, options_menu, print_formated_board, print_title
from helpers import random_char, random_name, is_char


# players cannot have same name or mark
PLAYERS: list[IPlayer] = []


def play_classic() -> None:
    # Pre game: variables inicialization
    while True:
        board = Board2D(3, 3)
        win_checker = ClassicWinChecker(board.board)
        players = {player: 0 for player in PLAYERS}  # Player and score
        # Set instances to players
        for player in players:
            player.set_board(board)
            player.set_win_checker(win_checker)
        players_cycle = cycle(players)  # Infinity iterable

        system('cls')
        print_title('the game will start')
        sleep(2)

        # Game loop
        while True:
            act_player = next(players_cycle)
            # Input loop
            while True:
                system('cls')
                print_formated_board(board.board)
                print(f"It's {act_player.name.upper()} turn -> {act_player.mark}")
                sleep(1)
                row, column = act_player.play()
                if not isinstance(row, int):
                    print(row)
                    sleep(2)
                    continue
                if not isinstance(column, int):
                    print(column)
                    sleep(2)
                    continue
                if (row, column) not in board.empty_places():
                    print('Choose a empty place')
                    sleep(2)
                    continue
                break
            board.place_mark(row, column, act_player.mark)
            if win_checker.check_win():
                system('cls')
                print_formated_board(board.board)
                print_title(f'{act_player.name} won!')
                sleep(2)
                end_game_menu = options_menu('play again', {'Yes': '', 'No': ''})
                match end_game_menu:
                    case 'Yes':
                        break
                    case 'No':
                        PLAYERS.clear()
                        return


def pick_ia_dificulty() -> IPlayer:
    dificulty_menu = options_menu('ia dificulty',
                                 {'Easy': '', 'Medium': '', 'Hard': '', 'Impossible': ''})
    match dificulty_menu:
        case 'Easy':
            dificulty = EasyPlayer
        case 'Medium':
            dificulty = MediumPlayer
        case 'Hard':
            dificulty = HardPlayer
        case 'Impossible':
            dificulty = ImpossiblePlayer
    return dificulty


def get_users_players(amount: int) -> None:
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


def classic_configuration() -> None:
    while True:
        players_menu = options_menu('classic mode | opponent',
                                   {'IA': 'Play against the computer. Custom dificulty',
                                    'Local': 'Local match up',
                                    'Back': ''})
        match players_menu:
            case 'IA':
                ia_dificulty = pick_ia_dificulty()

                # player profile
                get_users_players(1)

                # IA profile
                PLAYERS.append(ia_dificulty(name=random_name([player.name for player in PLAYERS]),
                                            mark=random_char([player.mark for player in PLAYERS])))
            case 'Local':
                # no IA profile
                get_users_players(2)
            case 'Back':
                return

        start_menu = options_menu('classic mode | start',
                                 {'Start': 'Players awaiting: {}'.format(str([player.name for player in PLAYERS]).replace("\'", "")),
                                  'Change settings': '',
                                  'Back': ''})
        match start_menu:
            case 'Start':
                play_classic()
            case 'Change settings':
                continue
            case 'Back':
                return


def game_modes() -> None:
    while True:
        game_mode_menu = options_menu('game modes',
                                     {'Classic': 'Two players against each other. 3x3 board. Classic win rules',
                                      'Teams': 'Up to five players on each team (two teams). board up to 12x12. Custom sequence win',
                                      'Back': ''})
        match game_mode_menu:
            case 'Classic':
                classic_configuration()
            case 'Teams':
                pass
            case 'Back':
                return


def main_menu() -> None:
    while True:
        main_menu = options_menu('main menu',
                                {'Play': '', 'Options': '', 'Quit': ''})
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
