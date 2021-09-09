"""This is the object which intakes a board, solves it, and then returns the
    solved board."""
from Board import Board


class Solver:

    def __init__(self, board: Board = None):
        self.board = board

    def __repr__(self):
        return str([row for row in self.board.rows])

    def solve_row(self, row_index):
        changed = False
        taken = [element.value for element in self.board.rows[row_index] if element.value is not None]
        for element in self.board.rows[row_index]:
            if element.solved:
                pass
            else:
                for value in taken:
                    safety = element.eliminate_possible(value)
                    if safety == "error":
                        return safety
        return "safe"

    def solve_col(self, col_index):
        changed = False
        taken = [element.value for element in self.board.columns[col_index] if element.value is not None]
        for element in self.board.columns[col_index]:
            if element.solved:
                pass
            else:
                for value in taken:
                    safety = element.eliminate_possible(value)
                    if safety[1] is True:
                        changed = True
                    if safety[0] == "error":
                        return "error"
        return "safe", changed