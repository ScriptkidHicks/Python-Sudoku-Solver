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

    def solve_sq(self, sq_index):
        changed = False
        taken = [element.value for element in self.board.squares[sq_index] if element.value is not None]
        for element in self.board.squares[sq_index]:
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

    def solve_by_rows(self):
        changed = False
        for x in range(9):
            safety = self.solve_row(x)
            if safety[1] is True:
                changed = True
            if safety[0] == "error":
                return "error", changed
        return "safe", changed

    def solve_by_cols(self):
        changed = False
        for x in range(9):
            safety = self.solve_col(x)
            if safety[1] is True:
                changed = True
            if safety[0] == "error":
                return "error", changed
        return "safe", changed

    def solve_by_squares(self):
        changed = False
        for x in range(9):
            safety = self.solve_sq(x)
            if safety[1] is True:
                changed = True
            if safety[0] == "error":
                return "error", changed
        return "safe", changed

    def naked_solve(self):
        changed = False
        safety = self.solve_by_rows()
        if safety[0] == "error":
            return "error", changed
        if safety[1] is True:
            changed = True
        safety = self.solve_by_cols()
        if safety[0] == "error":
            return "error", changed
        if safety[1] is True:
            changed = True
        safety = self.solve_by_squares()
        if safety[0] == "error":
            return "error", changed
        if safety[1] is True:
            changed = True
        return "safe", changed