from Board import Board
from BoardSolver import Solver

empty = [
    [0, 9, 0, 0, 3, 0, 1, 5, 0],
    [2, 1, 8, 7, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 4],
    [9, 0, 0, 0, 7, 8, 4, 0, 0],
    [1, 8, 5, 4, 2, 0, 7, 6, 0],
    [3, 7, 0, 0, 6, 0, 0, 2, 8],
    [0, 0, 1, 0, 0, 0, 0, 7, 0],
    [0, 0, 9, 0, 5, 7, 0, 0, 1],
    [8, 0, 7, 0, 0, 3, 0, 4, 0],
]

newBoard = Board()
newBoard.set_by_rows(empty)
mySolver = Solver(newBoard)
mySolver.naked_solve()
mySolver.naked_solve()
mySolver.naked_solve()
print()
newBoard.print_by_rows()