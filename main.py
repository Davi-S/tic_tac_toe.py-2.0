"""Main file. Meant do be run"""

# IMPORTS #
from itertools import cycle
from os import system
from time import sleep

# LOCAL IMPORTS #
import settings
from engine.player import EasyPlayer, HumanPlayer, IPlayer, MediumPlayer, HardPlayer, ImpossiblePlayer
from engine.win_check import ClassicWinChecker
from engine.board import Board2D
from menus import OpenMenu, OptionMenu, Opt
from helpers import random_char, random_name, is_char


# players cannot have same name or mark
PLAYERS: list[IPlayer] = []


# TODO: refactor this code using the new menus
def play_classic() -> None:
    pass
    # # Pre game: variables inicialization
    # while True:
    #     board = Board2D(3, 3)
    #     win_checker = ClassicWinChecker(board.board)
    #     players = {player: 0 for player in PLAYERS}  # Player and score
    #     # Set instances to players
    #     for player in players:
    #         player.set_board(board)
    #         player.set_win_checker(win_checker)
    #     players_cycle = cycle(players)  # Infinity iterable

    #     system('cls')
    #     print_title('the game will start')
    #     sleep(2)

    #     # Game loop
    #     while True:
    #         act_player = next(players_cycle)
    #         # Input loop
    #         while True:
    #             system('cls')
    #             print_formated_board(board.board)
    #             print(
    #                 f"It's {act_player.name.upper()} turn -> {act_player.mark}")
    #             sleep(1)
    #             row, column = act_player.play()
    #             if not isinstance(row, int):
    #                 print(row)
    #                 sleep(2)
    #                 continue
    #             if not isinstance(column, int):
    #                 print(column)
    #                 sleep(2)
    #                 continue
    #             if (row, column) not in board.empty_places():
    #                 print('Choose a empty place')
    #                 sleep(2)
    #                 continue
    #             break
    #         board.place_mark(row, column, act_player.mark)
    #         if win_checker.check_win():
    #             system('cls')
    #             print_formated_board(board.board)
    #             print_title(f'{act_player.name} won!')
    #             sleep(2)
    #             end_game_menu = options_menu(
    #                 'play again', {'Yes': '', 'No': ''})
    #             match end_game_menu:
    #                 case 'Yes':
    #                     break
    #                 case 'No':
    #                     PLAYERS.clear()
    #                     return


def start_menu():
    start_menu = OptionMenu('start game',
                            [Opt('Start',
                                 'Players awaiting: {}'.format(
                                     str([player.name for player in PLAYERS]).replace("\'", "")),
                                 {play_classic: {}}),
                             Opt('Back', '', 'return')],
                            one_time=True)
    start_menu.run()
    # Prevent player stack when option 'back'
    PLAYERS.clear()


def set_ia(dificulty: IPlayer) -> None:
    name = random_name([player.name for player in PLAYERS])
    mark = random_char([player.mark for player in PLAYERS])
    PLAYERS.append(dificulty(name, mark))
    OpenMenu('ia profile', 
             f'The IA is set\n\nName: {name}\nMark: {mark}',
             'Press Enter to continue').run()


def ia_configuration():
    ia_dificulty = OptionMenu('ia dificulty',
                              [Opt('Easy', '', {set_ia: {'dificulty': EasyPlayer}}),
                               Opt('Medium', '', {
                                   set_ia: {'dificulty': MediumPlayer}}),
                               Opt('Hard', '', {
                                   set_ia: {'dificulty': HardPlayer}}),
                               Opt('Impossible', '', {set_ia: {'dificulty': ImpossiblePlayer}})],
                              one_time=True)
    ia_dificulty.run()


def set_players(quantity: int):
    count = 1
    while count <= quantity:
        text = 'Your profile' if quantity == 1 else f'Set {count}º player profile'

        name = OpenMenu('player profile', text, 'Nickname: ').run()
        mark = OpenMenu('player profile', text, 'Mark: ').run()

        if not is_char(mark):
            print('The mark must be one letter')
            sleep(settings.SLEEP_TIME)
            continue
        if mark in [player.mark for player in PLAYERS]:
            print('This mark is alread in use')
            sleep(settings.SLEEP_TIME)
            continue
        if name in [player.name for player in PLAYERS]:
            print('This name is alread in use')
            sleep(settings.SLEEP_TIME)
            continue

        PLAYERS.append(HumanPlayer(name, mark))
        count += 1


def classic_configuration(opponent: str):
    """Sequence of functions before start the game

    Args:
        opponent (str): IA or Local
    """
    match opponent:
        case 'IA':
            ia_configuration()
            set_players(1)
        case 'Local':
            set_players(2)

    start_menu()


def classic_settings() -> None:
    players_menu = OptionMenu('classic mode settings',
                              [Opt('IA', 'Play against the computer. Custom dificulty',
                                   {classic_configuration: {'opponent': 'IA'}}),
                               Opt('Local', 'Local match up',
                                   {classic_configuration: {'opponent': 'Local'}}),
                               Opt('Back', '', 'return')])
    players_menu.run()


def game_modes() -> None:
    game_mode_menu = OptionMenu('game modes',
                                [Opt('Classic', 'Two players against each other. 3x3 board. Classic win rules', {classic_settings: {}}),
                                 Opt('Teams', 'Up to five players on each team (two teams). board up to 12x12. Custom sequence win', ''),
                                 Opt('Back', '', 'return')])
    game_mode_menu.run()


def main_menu() -> None:
    main_menu = OptionMenu('main menu',
                           [Opt('Play', '', {game_modes: {}}),
                            Opt('Settings', '', ''),
                            Opt('Quit', '', {quit: {}})])
    main_menu.run()


def main() -> int:
    system('cls')
    main_menu()
    return 0


if __name__ == '__main__':
    main()
