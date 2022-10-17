"""Board concrete classes"""

# standard library imports #
# related third party imports #
# local application/library specific imports #


BOARD_HINT = list[list]


class Board:
    """Two dimensional array"""

    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self._board = self._create_board(rows, columns)

    @property
    def board(self) -> BOARD_HINT:
        return self._board

    def place_mark(self, row: int, column: int, mark: str, rewrite: bool = False) -> bool:
        """Place a mark on the board

        Args:
            line (int): x axis
            column (int): y axis
            mark (str): The mark to place
            rewrite (bool, optional): Replace the current mark with the selected one. Defaults to False.

        Returns:
            bool: True if the marks was sucessfuly placed. False if the mark could not be placed
        """
        if rewrite or self._board[row][column] is None:
            self._board[row][column] = mark
            return True
        return False

    def _create_board(self, rows: int, columns: int) -> BOARD_HINT:
        """Create a empty two dimention matrix (board)"""
        gridline = [None for _ in range(rows)]
        gridline = [list(gridline) for _ in range(columns)]
        return gridline

    def empty_places(self) -> list[tuple[int, int]]:  # sourcery skip: for-append-to-extend
        """Get the board empty places

        Returns:
            list[tuple[int, int]]: List of Empty coordinates
        """
        empty_places = []
        for row_idx, row in enumerate(self.board):
            for column_idx, column in enumerate(row):
                if column is None:
                    empty_places.append((row_idx, column_idx))
        return empty_places
    
    def is_terminal(self):
        return len(self.empty_places()) == 0
            
