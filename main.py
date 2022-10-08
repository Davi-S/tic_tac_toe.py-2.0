"""Main file. Meant do be run"""

# IMPORTS #
from os import system
from time import sleep

# LOCAL IMPORTS #
import settings
from engine.player import IPlayer, HumanPlayer, EasyPlayer, MediumPlayer, HardPlayer, ImpossiblePlayer
from game_modes import play_classic
from menus import IndependentOpenMenu, NestedOpenMenu, NestedOptionMenu, Opt
from helpers import random_char, random_name, is_char


# players cannot have same name or mark
PLAYERS: list[IPlayer] = []


def start_menu():
    start_menu = NestedOptionMenu('start game',
                           [Opt('Start',
                                 'Players awaiting: {}'.format(str([player.name for player in PLAYERS]).replace("\'", "")),
                                 {play_classic: {'player_list': PLAYERS}}),
                            Opt('Back',
                                '',
                                'return')],
                            one_time=True)
    start_menu.run()
    # Prevent player stack when option 'back'
    PLAYERS.clear()


def set_ia(dificulty: IPlayer) -> None:
    name = random_name([player.name for player in PLAYERS])
    mark = random_char([player.mark for player in PLAYERS])
    PLAYERS.append(dificulty(name, mark))
    IndependentOpenMenu('ia profile',
                   f'The IA is set\n\nName: {name}\nMark: {mark}',
                   'Press Enter to continue').run()


def ia_configuration():
    ia_dificulty = NestedOptionMenu('ia dificulty',
                              [Opt('Easy', '',
                                   {set_ia: {'dificulty': EasyPlayer}}),
                               Opt('Medium', '', 
                                   {set_ia: {'dificulty': MediumPlayer}}),
                               Opt('Hard', '', 
                                   {set_ia: {'dificulty': HardPlayer}}),
                               Opt('Impossible', '', 
                                   {set_ia: {'dificulty': ImpossiblePlayer}})],
                              one_time=True)
    ia_dificulty.run()


def set_players(quantity: int):
    count = 1
    while count <= quantity:
        text = 'Your profile' if quantity == 1 else f'Set {count}º player profile'

        name = NestedOpenMenu('player profile', text, 'Nickname: ').run()
        mark = NestedOpenMenu('player profile', text, 'Mark: ').run()

        if not is_char(mark):
            print('The mark must be one letter')
            sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        if mark in [player.mark for player in PLAYERS]:
            print('This mark is alread in use')
            sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        if name in [player.name for player in PLAYERS]:
            print('This name is alread in use')
            sleep(settings.MEDIUM_SLEEP_TIME)
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
    players_menu = NestedOptionMenu('classic mode settings',
                              [Opt('IA', 'Play against the computer. Custom dificulty',
                                   {classic_configuration: {'opponent': 'IA'}}),
                               Opt('Local', 'Local match up',
                                   {classic_configuration: {'opponent': 'Local'}}),
                               Opt('Back', '',
                                   'return')])
    players_menu.run()


def game_modes() -> None:
    game_mode_menu = NestedOptionMenu('game modes',
                                [Opt('Classic', 'Two players against each other. 3x3 board. Classic win rules', {classic_settings: {}}),
                                 Opt('Teams', 'Up to five players on each team (two teams). board up to 12x12. Custom sequence win', None),
                                 Opt('Back', '', 'return')])
    game_mode_menu.run()


def main_menu() -> None:
    main_menu = NestedOptionMenu('main menu',
                           [Opt('Play', '', {game_modes: {}}),
                            Opt('Settings', '', None),
                            Opt('Quit', '', {quit: {}})])
    main_menu.run()


def main() -> int:
    system('cls')
    main_menu()
    return 0


if __name__ == '__main__':
    main()
