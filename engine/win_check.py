"""WinCheker concrete classes"""

# standard library imports #
# related third party imports #
# local application/library specific imports #
import abstracts
import engine.board as bd
import helpers as hp


class WinChecker(abstracts.IWinChecker):
    """A row, column of great diagonal if fully filled with only one mark"""
    # TODO: add comments on this class

    def __init__(self, board_state: bd.BOARD_HINT, sequence_len: int) -> None:
        super().__init__(board_state)
        self.sequence_len = sequence_len

    def check_win(self) -> bool:
        """Check if there is a win on the game

        Returns:
            bool: True is there is a win. False is there is no win
        """
        win_info = self.win_info()
        return any(value != None for value in win_info.values())

    def win_info(self) -> dict:
        """The information about a win

        Returns:
            dict: {group: (mark, index)}
        """
        return {'row': self._get_row_winner(), 'column': self._get_column_winner(), 'p_diagonal': self._get_p_diagonal_winner(), 's_diagonal': self._get_s_diagonal_winner()}

    def _win_condition(self, val: int) -> bool:
        """Check if the win condition is true

        Args:
            group (list): A row, column or great diagonal of the board state

        Returns:
            bool: True is the win condition is true. False if the win condition is false
        """
        return val >= self.sequence_len
    
    def _check_group(self, group: list) -> list[dict]:
        """Return information about wins in the given group

        Args:
            group (list): a column, row or diagonal

        Returns:
            list[dict]: list with dictionary containing: mark, sequence_info, group_idx
        """
        checked = set()
        data = []
        for mark in group:
            if (mark != None) and (mark not in checked):
                data.append({'mark': mark, 'sequence': hp.longest_consecutive_occourence(group, mark)})
                checked.add(mark)

        return [i for i in data if self._win_condition(i['sequence'][0])]

    def _get_winner(self, group_list: list) -> dict:
        """Return information about wins in the given group list

        Args:
            group_list (list): a list containing groups

        Returns:
            dict: mark, sequence_info, group_idx
        """
        for idx, group in enumerate(group_list):
            if winner := self._check_group(group):
                winner[0]['group_idx'] = idx
                return winner
        return None
        
    def _get_row_winner(self) -> dict:
        """Return information about wins in the rows

        Returns:
            dict: mark, sequence_info, group_idx
        """
        return self._get_winner(hp.Matrix(self.board_state).rows())
    
    def _get_column_winner(self) -> dict:
        """Return information about wins in the columns

        Returns:
            dict: mark, sequence_info, group_idx
        """
        return self._get_winner(hp.Matrix(self.board_state).columns())

    def _get_p_diagonal_winner(self) -> dict:
        """Return information about wins in the primary diagonals

        Returns:
            dict: mark, sequence_info, group_idx
        """
        return self._get_winner(hp.Matrix(self.board_state).p_diagonals())

    def _get_s_diagonal_winner(self) -> dict:
        """Return information about wins in the secondary diagonals

        Returns:
            dict: mark, sequence_info, group_idx
        """
        return self._get_winner(hp.Matrix(self.board_state).s_diagonals())



def main() -> int:
    return 0


if __name__ == '__main__':
    main()
