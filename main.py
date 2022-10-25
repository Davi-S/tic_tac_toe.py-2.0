"""Main file. Meant do be run"""

# standard library imports #
import os
import time as tm

# related third party imports #
# local application/library specific imports #
import abstracts as ab
import engine.player as plr
import game_modes as gm
import helpers as hp
import menus as mn
import settings


PLAYERS: list[ab.IPlayer] = []
BOARD_SIZE = 3
WIN_SEQUENCE = 3


def start_menu(game_mode: ab.IGame, **kwargs) -> None:
    start_menu = mn.NestedOptionMenu('start game',
                           [mn.Opt('Start',
                                'Players awaiting: {}'.format(str([player.name for player in PLAYERS]).replace("\'", "")),
                                {game_mode: kwargs | {'player_list': PLAYERS}}),
                            mn.Opt('Back',
                                '',
                                'return')],
                           one_time=True)
    start_menu.run()
    
    # Prevent player stack when choose option 'back'
    PLAYERS.clear()


def set_ia(dificulty: ab.IPlayer) -> None:
    name = hp.random_name([player.name for player in PLAYERS])
    mark = hp.random_char([player.mark for player in PLAYERS])
    PLAYERS.append(dificulty(name, mark))
    mn.IndependentOpenMenu('ia profile',
                           f'The IA is set\n\nName: {name}\nMark: {mark}',
                           'Press Enter to continue').run()


def ia_configuration() -> None:
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


def set_players(quantity: int) -> None:
    count = 1
    while count <= quantity:
        text = 'Your profile' if quantity == 1 else f'Set {count}º player profile'

        name = mn.NestedOpenMenu('player profile', text, 'Nickname: ').run()
        mark = mn.NestedOpenMenu('player profile', text, 'Mark: ').run()

        if not hp.is_char(mark):
            print('The mark must be one letter')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        if mark in [player.mark for player in PLAYERS]:
            print('This mark is alread in use')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        if name in [player.name for player in PLAYERS]:
            print('This name is alread in use')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue

        PLAYERS.append(plr.HumanPlayer(name, mark))
        count += 1


def classic_configuration(opponent: str) -> None:
    match opponent:
        case 'IA':
            ia_configuration()
            set_players(1)
        case 'Local':
            set_players(2)

    start_menu(gm.SimpleGame)


def classic_settings() -> None:
    players_menu = mn.NestedOptionMenu('classic mode settings',
                              [mn.Opt('IA', 'Play against the computer. Custom dificulty',
                                   {classic_configuration: {'opponent': 'IA'}}),
                               mn.Opt('Local', 'Local match up',
                                   {classic_configuration: {'opponent': 'Local'}}),
                               mn.Opt('Back', '',
                                   'return')])
    players_menu.run()


def board_configuration() -> None:
    global BOARD_SIZE
    while True:
        board_size = mn.NestedOpenMenu('choose board size', '', 'board size: ').run()
        try:
            board_size = int(board_size)
        except ValueError:
            print('Pick a valid board size. Beetwen 3 and 12')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue
            
        if not 3 <= board_size <= 12:
            print('Pick a valid board size. Beetwen 3 and 12')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        
        BOARD_SIZE = board_size
        return
    
    
def win_sequence_configuration() -> None:
    global WIN_SEQUENCE
    while True:
        win_sequence = mn.NestedOpenMenu('choose win sequence size', '', 'win sequence size: ').run()
        
        try:
            win_sequence = int(win_sequence)
        except ValueError:
            print(f'Pick a valid win sequence size. Beetwen 3 and {BOARD_SIZE} (board size)')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        
        if not 3 <= win_sequence <= BOARD_SIZE:
            print(f'Pick a valid win sequence size. Beetwen 3 and {BOARD_SIZE}')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        
        WIN_SEQUENCE = win_sequence
        return


def custom_players_configuration() -> None:
    while True:
        local_players_amount = mn.NestedOpenMenu('Local Players number', 'How many local players are going to play', 'amout: ').run()
        IA_amount = mn.NestedOpenMenu('IA Players number', 'How many IA are going to play (easy difficulty)', 'amout: ').run()
        try:
            local_players_amount = int(local_players_amount)
            IA_amount = int(IA_amount)
        except ValueError:
            print('Pick a valid integer number')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        
        total = local_players_amount + IA_amount
            
        if not 2 <= total <= 5:
            print('Pick a valid total players amout. Beetwen 2 and 5')
            tm.sleep(settings.MEDIUM_SLEEP_TIME)
            continue
        
        for _ in range(IA_amount):
            set_ia(plr.EasyPlayer)
            
        set_players(local_players_amount)
        return


def custom_start() -> None:
    if PLAYERS:
        print('\n\nActual settings')
        print(f'Board size: {BOARD_SIZE}\nWin sequence: {WIN_SEQUENCE}')
        tm.sleep(settings.LONG_SLEEP_TIME)
        start_menu(gm.SimpleGame, board_size = BOARD_SIZE, win_sequence = WIN_SEQUENCE)
        return

    print('Set players before start a game')
    tm.sleep(settings.MEDIUM_SLEEP_TIME)


def custom_settings() -> None:
    players_menu = mn.NestedOptionMenu('custom mode settings',
                              [mn.Opt('Board size', 'Default to 3',
                                   {board_configuration: {}}),
                               mn.Opt('Win sequence size', 'How many marks in a row to win. Default to 3',
                                   {win_sequence_configuration: {}}),
                               mn.Opt('Players', 'Set players profile',
                                   {custom_players_configuration: {}}),
                               mn.Opt('Start', 'Start game',
                                   {custom_start: {}}),
                               mn.Opt('Back', '',
                                   'return')])
    players_menu.run()


def ia_adapt_settings() -> None:
    set_ia(plr.EasyPlayer)
    set_players(1)
    start_menu(gm.AdaptativeGame)
    


def game_modes() -> None:
    game_mode_menu = mn.NestedOptionMenu('game modes',
                                [mn.Opt('Classic', 'Two players against each other. 3x3 board. Classic win rules. 3 IA difficulties', {classic_settings: {}}),
                                 mn.Opt('Free for All', 'Up to five players against each other. board up to 12x12. Custom sequence win. 1 IA difficulty', {custom_settings: {}}),
                                 mn.Opt('Adaptative IA', 'Play agains the IA. The IA will adapt to your level each game for a skill match based', {ia_adapt_settings: {}}),
                                 mn.Opt('Back', '', 'return')])
    game_mode_menu.run()


def main_menu() -> None:
    main_menu = mn.NestedOptionMenu('main menu',
                           [mn.Opt('Play', '', {game_modes: {}}),
                            mn.Opt('Quit', '', 'return')])
    main_menu.run()


def main() -> int:
    os.system('cls')
    main_menu()
    return 0


if __name__ == '__main__':
    main()
