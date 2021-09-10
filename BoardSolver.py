"""This is the object which intakes a board, solves it, and then returns the
    solved board."""
from Board import Board
from Tile import Tile


class Solver:

    def __init__(self, board: Board = None):
        self.board = board

    def __repr__(self):
        return str([row for row in self.board.rows])

    def check_solved(self):
        for row in self.board.rows:
            for element in row:
                if not element.solved:
                    return "Board not Solved"
        return "Board Solved"

    def naked_group_solve(self, group: list[Tile]):
        changed = False
        taken = [element.value for element in group if element.solved]
        for element in group:
            if not element.solved:
                for value in taken:
                    check = element.eliminate_possible(value)
                    if check[0] == "error":
                        return "error", changed
                    elif check[1] is True:
                        changed = True
        return "safe", changed

    def hidden_group_solve(self, group: list[Tile]):
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        changed = False
        for number in choices:
            possible_tiles = []
            for tile in group:
                if not tile.solved and (number in tile.possibles):
                    possible_tiles.append(tile)
                    changed = True
            if len(possible_tiles) == 1:
                possible_tiles[0].set_value(number)
        return "safe", changed

    def function_solve(self, solve_method):
        changed = False
        for row in self.board.rows:
            check = solve_method(row)
            if check[0] == "error":
                return "error", changed
            elif check[1] is True:
                changed = True
        for col in self.board.columns:
            check = solve_method(col)
            if check[0] == "error":
                return "error", changed
            elif check[1] is True:
                changed = True
        for square in self.board.squares:
            check = solve_method(square)
            if check[0] == "error":
                return "error", changed
            elif check[1] is True:
                changed = True
        return "safe", changed

    def solve_board(self):
        changed = True
        while changed:
            changed = False
            check = self.function_solve(self.naked_group_solve)
            if check[0] == "error":
                quit("Solve Error")
            elif check[1] is True:
                changed = True
            check = self.function_solve(self.hidden_group_solve)
            if check[0] == "error":
                quit("Solve Error")
            elif check[1] is True:
                changed = True
        print(self.check_solved())
        return
