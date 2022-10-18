"""Main file. Meant do be run"""

# standard library imports #
from os import system
from time import sleep

# related third party imports #
# local application/library specific imports #
import abstracts
import engine.player as plr
import game_modes as gm
import helpers as hp
import menus as mn
import settings

# TODO: IMPORTANT
# add more comments to code

# players cannot have same name or mark
PLAYERS: list[abstracts.IPlayer] = []


def start_menu():
    start_menu = mn.NestedOptionMenu('start game',
                           [mn.Opt('Start',
                                'Players awaiting: {}'.format(str([player.name for player in PLAYERS]).replace("\'", "")),
                                {gm.ClassicGame: {'player_list': PLAYERS}}),
                            mn.Opt('Back',
                                '',
                                'return')],
                           one_time=True)
    start_menu.run()
    # Prevent player stack when option 'back'
    PLAYERS.clear()


def set_ia(dificulty: abstracts.IPlayer) -> None:
    name = hp.random_name([player.name for player in PLAYERS])
    mark = hp.random_char([player.mark for player in PLAYERS])
    PLAYERS.append(dificulty(name, mark))
    mn.IndependentOpenMenu('ia profile',
                   f'The IA is set\n\nName: {name}\nMark: {mark}',
                   'Press Enter to continue').run()


def ia_configuration():
    ia_dificulty = mn.NestedOptionMenu('ia dificulty',
                              [mn.Opt('Easy', '',
                                   {set_ia: {'dificulty': plr.EasyPlayer}}),
                               mn.Opt('Medium', '', 
                                   {set_ia: {'dificulty': plr.MediumPlayer}}),
                               mn.Opt('Hard', '', 
                                   {set_ia: {'dificulty': plr.HardPlayer}}),
                               mn.Opt('Impossible', '', 
                                   {set_ia: {'dificulty': plr.ImpossiblePlayer}})],
                              one_time=True)
    ia_dificulty.run()


def set_players(quantity: int):
    count = 1
    while count <= quantity:
        text = 'Your profile' if quantity == 1 else f'Set {count}º player profile'

        name = mn.NestedOpenMenu('player profile', text, 'Nickname: ').run()
        mark = mn.NestedOpenMenu('player profile', text, 'Mark: ').run()

        if not hp.is_char(mark):
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

        PLAYERS.append(plr.HumanPlayer(name, mark))
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
    players_menu = mn.NestedOptionMenu('classic mode settings',
                              [mn.Opt('IA', 'Play against the computer. Custom dificulty',
                                   {classic_configuration: {'opponent': 'IA'}}),
                               mn.Opt('Local', 'Local match up',
                                   {classic_configuration: {'opponent': 'Local'}}),
                               mn.Opt('Back', '',
                                   'return')])
    players_menu.run()


def game_modes() -> None:
    game_mode_menu = mn.NestedOptionMenu('game modes',
                                [mn.Opt('Classic', 'Two players against each other. 3x3 board. Classic win rules', {classic_settings: {}}),
                                 mn.Opt('Teams', 'Up to five players on each team (two teams). board up to 12x12. Custom sequence win', None),
                                 mn.Opt('Back', '', 'return')])
    game_mode_menu.run()


def main_menu() -> None:
    main_menu = mn.NestedOptionMenu('main menu',
                           [mn.Opt('Play', '', {game_modes: {}}),
                            mn.Opt('Settings', '', None),
                            mn.Opt('Quit', '', 'return')])
    main_menu.run()


def main() -> int:
    system('cls')
    main_menu()
    return 0


if __name__ == '__main__':
    main()
