"""WinCheker concrete classes"""

# IMPORTS #

# LOCAL IMPORTS #
import abstracts
import helpers as hp


class WinChecker(abstracts.IWinChecker):
    """A row, column of great diagonal if fully filled with only one mark"""

    def __init__(self, board_state: abstracts.BOARD_HINT, sequence_len: int) -> None:
        super().__init__(board_state)
        self.sequence_len = sequence_len

    def check_win(self) -> bool:
        """Check if there is a win on the game

        Returns:
            bool: True is there is a win. False is there is no win
        """
        win_info = self.get_win_info()
        return any(value[0] != None for value in win_info.values())

    def get_win_info(self) -> dict:
        """The information about a win

        Returns:
            dict: {group: (mark, index)}
        """
        return {'row': self._get_row_winner(), 'column': self._get_column_winner(), 'p_diagonal': self._get_p_diagonal_winner(), 's_diagonal': self._get_s_diagonal_winner()}

    def _win_condition(self, group: list) -> bool:
        """Check if the win condition is true

        Args:
            group (list): A row, column or great diagonal of the board state

        Returns:
            bool: True is the win condition is true. False if the win condition is false
        """
        data = {mark: hp.longest_consecutive_occourence(
            group, mark) for mark in group if mark != None}
        return [key for key, value in data.items() if value >= self.sequence_len]

        # return len(set(group)) == 1 and set(group) != {None}

    # sourcery skip: use-next
    def _get_row_winner(self) -> tuple[str | None, int]:
        """Return the mark that won on any row of the board.
        If none won, return None and a negative index

        Returns:
            tuple[str, int]: str: the mark that won. int: index of the row won
        """
        for idx, row in enumerate(hp.Matrix.rows(self.board_state)):
            if winner := self._win_condition(row):
                # return the mark and the index of the row where it won
                return winner, idx
        return None, -1

    # sourcery skip: use-next
    def _get_column_winner(self) -> tuple[str | None, int]:
        """Return the mark that won on any column of the board.
        If none won, return None and a negative index

        Returns:
            tuple[str, int]: str: the mark that won. int: index of the column won
        """
        for idx, column in enumerate(hp.Matrix.columns(self.board_state)):
            if winner := self._win_condition(column):
                # return the mark and the index of the column where it won
                return winner, idx
        return None, -1

    def _get_p_diagonal_winner(self) -> tuple[str | None, int]:
        """Return the mark that won in the primary diagonal of the board.
        If none won, return None and a negative index

        Returns:
            tuple[str, int]: str -> the mark that won. int -> index of the diagonal won:
            0 for the primary diagonal and 1 for the secundary diagonal
        """
        for idx, diagonal in enumerate(hp.Matrix.p_diagonals(self.board_state)):
            if winner := self._win_condition(diagonal):
                # return the mark and the index of the column where it won
                return winner, idx
        return None, -1

    def _get_s_diagonal_winner(self) -> tuple[str | None, int]:
        """Return the mark that won on the secundary diagonal of the board.
        If none won, return None and a negative index

        Returns:
            tuple[str, int]: str -> the mark that won. int -> index of the diagonal won:
            0 for the primary diagonal and 1 for the secundary diagonal
        """
        for idx, diagonal in enumerate(hp.Matrix.s_diagonals(self.board_state)):
            if winner := self._win_condition(diagonal):
                # return the mark and the index of the column where it won
                return winner, idx

        return None, -1


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
