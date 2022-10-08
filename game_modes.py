"""Game modes loops"""

# IMPORTS #
from os import system
from time import sleep
from itertools import cycle

# LOCAL IMPORTS #
import settings
from engine.board import Board2D
from engine.win_check import ClassicWinChecker
from engine.player import EasyPlayer, HumanPlayer, IPlayer
from menus import Opt, IndependentOptMenu, IndependentOpenMenu, print_title
from helpers import print_formated_board


def score_format(data: dict[IPlayer, int]):
    result = ''
    for player, score in data.items():
        result += f'{player.name} [ {player.mark} ] >>> {score}\n'
    return result


# TODO: refactor this code using the new menus
def play_classic(player_list: list[IPlayer]) -> None:
    players = {player: 0 for player in player_list}  # Player and score
    players_cycle = cycle(players)  # Infinity iterable
    
    while True:
        board = Board2D(3, 3)
        win_checker = ClassicWinChecker(board.board)
        # Set instances to players
        for player in player_list:
            player.set_board(board)
            player.set_win_checker(win_checker)
            
        system('cls')
        print_title('starting the game')
        sleep(settings.SHORT_SLEEP_TIME)

        while True:  # Game loop
            act_player = next(players_cycle)
            while True:  # Input loop
                system('cls')
                print_formated_board(board.board)
                print(f"It's {act_player.name.upper()} turn -> {act_player.mark}")
                sleep(settings.SHORT_SLEEP_TIME)
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
                players[act_player] += 1  # increase score
                
                system('cls')
                print_formated_board(board.board)
                print_title(f'{act_player.name} won!')
                sleep(settings.MEDIUM_SLEEP_TIME)
                system('cls')
                
                IndependentOpenMenu('Score', score_format(players), 'Press Enter to continue').run()
                
                end_game = IndependentOptMenu('play again',
                                   [Opt('Yes', '', 'Yes'),
                                    Opt('No', '', 'No')]).run()
                match end_game:
                    case 'Yes':
                        break
                    case 'No':
                        return
                    
def main() -> int:
    return 0


if __name__ == '__main__':
    main()