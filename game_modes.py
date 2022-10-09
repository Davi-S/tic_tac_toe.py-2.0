"""Game modes loops"""

# IMPORTS #
from os import system
from time import sleep
from itertools import cycle

# LOCAL IMPORTS #
import settings
import abstracts
import engine.board as bd
import engine.win_check as wc
import engine.player as plr
import menus as mn
import helpers as hp


def score_format(data: dict[abstracts.IPlayer, int]):
    return ''.join(f'{player.name} [ {player.mark} ] >>> {score}\n' for player, score in data.items())


class ClassicGame:
    def __init__(self, player_list: list[abstracts.IPlayer]) -> None:
        self.players_score = {player: 0 for player in player_list}
        self.players_cycle = cycle(player_list)
        self.act_player = None
        self.board_size = 3
        self.win_sequence = 3
        self.board = None
        self.win_checker = None

        # Set instances to players
        for player in self.players_score:
            player.set_game(self)

        self.run()

    def pre_match(self) -> None:
        """Create new board"""
        self.board = bd.Board(self.board_size, self.board_size)
        self.win_checker = wc.WinChecker(self.board.board, self.win_sequence)

    def get_play(self):
        while True:  # Input loop
            system('cls')
            hp.print_formated_board(self.board.board)
            print(f"It's {self.act_player.name.upper()} turn -> {self.act_player.mark}")
            sleep(settings.SHORT_SLEEP_TIME)
            row, column = self.act_player.play()
            if not isinstance(row, int):
                print(row)
                sleep(2)
                continue
            if not isinstance(column, int):
                print(column)
                sleep(2)
                continue
            if (row, column) not in self.board.empty_places():
                print('Choose a empty place')
                sleep(2)
                continue
            return row, column

    def match(self):
        self.pre_match()
        while True:
            self.act_player = next(self.players_cycle)
            row, column = self.get_play()
            self.board.place_mark(row, column, self.act_player.mark)
            if self.win_checker.check_win():
                self.players_score[self.act_player] += 1
                system('cls')
                hp.print_formated_board(self.board.board)
                mn.print_title(f'{self.act_player.name.upper()} won!')
                sleep(settings.MEDIUM_SLEEP_TIME)
                mn.IndependentOpenMenu('Score',
                                    score_format(self.players_score),
                                    'Press Enter to continue').run()
                return

            elif self.board.is_terminal():
                system('cls')
                hp.print_formated_board(self.board.board)
                mn.print_title('draw'.upper())
                sleep(settings.MEDIUM_SLEEP_TIME)
                mn.IndependentOpenMenu('Score',
                                    score_format(self.players_score),
                                    'Press Enter to continue').run()
                return

    def run(self):
        while True:
            self.match()
            new_game_menu = mn.IndependentOptionMenu('play again',
                                               [mn.Opt('Yes', '', 'Yes'),
                                                mn.Opt('No', '', 'No')]).run()
            match new_game_menu:
                case 'Yes':
                    continue
                case 'No':
                    return
            return


def main() -> int:
    game = ClassicGame([plr.HumanPlayer('Davi', 'x'), plr.MediumPlayer('Bot', 'o')])
    game.run()
    return 0


if __name__ == '__main__':
    main()
