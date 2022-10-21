"""Game modes loops"""

# standard library imports #
from itertools import cycle
from math import cos, sqrt
from os import system
from time import sleep

# related third party imports #
# local application/library specific imports #
import abstracts
import engine.board as bd
import engine.player as plr
import engine.win_check as wc
import helpers as hp
import menus as mn
import settings


class ClassicGame:
    def __init__(self, player_list: list[abstracts.IPlayer], board_size=3, win_sequence=3) -> None:
        self.player_list = player_list
        self.players_score = {player: 0 for player in self.player_list}
        self.matchs_played = 0
        self.players_cycle = cycle(self.player_list)
        self.act_player = None
        self.board_size = board_size
        self.win_sequence = win_sequence
        self.board = None
        self.win_checker = None

        # Set instances to players
        for player in self.players_score:
            player.set_game(self)

        # The game starts with the class instance creation
        self.run()

    def pre_match(self) -> None:
        """Create new board and win checker"""
        self.board = bd.Board(self.board_size, self.board_size)
        self.win_checker = wc.WinChecker(self.board.board, self.win_sequence)

    def get_play(self):
        while True:  # Input loop
            system('cls')
            hp.print_formated_board(self.board.board)
            print(f"It's {self.act_player.name.upper()} turn -> {self.act_player.mark}")
            sleep(settings.SHORT_SLEEP_TIME)
            row, column = self.act_player.play()
            
            # If the return is not a int, it is a error message (str)
            if not isinstance(row, int):
                print(row)
                sleep(2)
                continue
            if not isinstance(column, int):
                print(column)
                sleep(2)
                continue
            
            # Check for valid play
            if (row, column) not in self.board.empty_places():
                print('Choose a empty place')
                sleep(2)
                continue
            return row, column

    def match(self):
        self.pre_match()
        while True:
            self.act_player = next(self.players_cycle)  # Change players
            row, column = self.get_play()
            self.board.place_mark(row, column, self.act_player.mark)
            
            if self.win_checker.check_win():
                self.players_score[self.act_player] += 1  # Add score
                self.matchs_played += 1
                system('cls')
                hp.print_formated_board(self.board.board)
                mn.print_title(f'{self.act_player.name.upper()} won!')
                sleep(settings.MEDIUM_SLEEP_TIME)
                
                # Show score until press enter
                mn.IndependentOpenMenu('Score',
                                       self.score_format(),
                                       'Press Enter to continue').run()
                return

            elif self.board.is_terminal():  # Draw
                self.matchs_played += 1
                system('cls')
                hp.print_formated_board(self.board.board)
                mn.print_title('draw'.upper())
                sleep(settings.MEDIUM_SLEEP_TIME)
                
                # Show score until press enter
                mn.IndependentOpenMenu('Score',
                                       self.score_format(),
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
        
    def score_format(self):
        a = ''.join(f'TOTAL MATCHS: {self.matchs_played}\n\n')
        b = ''.join(f'{player.name} [ {player.mark} ] >>> {score}\n' for player, score in self.players_score.items())
        c = ''.join(f'\nDRAWS: {self.matchs_played - sum(self.players_score.values())}')
        return a + b + c


class AdaptativeGame(ClassicGame):
    def __init__(self, player_list: list[abstracts.IPlayer], board_size=3, win_sequence=3, mmr: int = 0) -> None:
        self.mmr = mmr
        super().__init__(player_list, board_size, win_sequence)
    
    def get_play(self):
        # Just like the super class. Differs if it is IA turn
        while True:  # Input loop
            system('cls')
            hp.print_formated_board(self.board.board)
            print(f"It's {self.act_player.name.upper()} turn -> {self.act_player.mark}")
            sleep(settings.SHORT_SLEEP_TIME)
            
            # If is IA turn, play with the current difficulty
            if isinstance(self.act_player, plr.ImpossiblePlayer):
                row, column = self.act_player.play(round(self.mmr))
            else:
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

    def pre_match(self) -> None:
        # Like the super class. Differs by calculate the MMR before game starts 
        self.calc_mmr()
        self.board = bd.Board(self.board_size, self.board_size)
        self.win_checker = wc.WinChecker(self.board.board, self.win_sequence)

    def calc_mmr(self) -> None:
        try:
            empty = len(self.board.empty_places()) + 1  # 1 to 5
        except AttributeError:
            empty = 1
            
        if isinstance(list(self.players_score)[0], plr.HumanPlayer):
            player_score = self.players_score[list(self.players_score)[0]]
            ia_score = self.players_score[list(self.players_score)[1]]
        else:
            player_score = self.players_score[list(self.players_score)[1]]
            ia_score = self.players_score[list(self.players_score)[0]]
        
        draws = self.matchs_played - sum(self.players_score.values())
        
        score_rel = player_score * 3 - ((ia_score + (draws)) * 6)
        
        mmr = score_rel * (1 / (empty * 2))
        
        self.mmr += mmr
        return
    
def main() -> int:
    game = AdaptativeGame([plr.HumanPlayer('Davi', 'x'), plr.ImpossiblePlayer('Bot', 'o')])
    game.run()
    return 0


if __name__ == '__main__':
    main()
