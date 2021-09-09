"""This is the board object. It contains some definitions about how we want
the board to represent and operate. Still pretty simple."""
from typing import List
from Tile import Tile


class Board:

    def __init__(self):
        """We won't initialize values in the board in here. This allows us to
        set the board by various methods later."""
        self.rows = None
        self.columns = None
        self.squares = None
        # max is useful as a way to track range for iteration, and also as a way
        # to track the maximum number in any spot.
        self.max = 0

    def set_by_rows(self, input_rows: List[List[int]]):
        self.max = len(input_rows)
        self.rows = []

        for row_index, row in enumerate(input_rows):
            self.rows.append([])
            for value in row:
                self.rows[row_index].append(Tile(value))

        # Now that we have the rows set, we can reference them to build the
        # columns

        self.columns = [[self.rows[y][x] for y in range(self.max)] for x in range(self.max)]
        # Python list comprehension, while slow, rocks

        # This one is a little trickier. Formally the squares are indexed left
        # to right, top to bottom:
        # [[ 1, 2, 3 ]
        #  [ 4, 5, 6 ]
        #  [ 7, 8, 9 ]]

        self.squares = []
        for x in range(9):
            appendage = []
            for y in range(9):
                appendage.append(None)
            self.squares.append(appendage)

            # this solution is extremely clever, and I am proud of myself
        for yCoord in range(9):
            for xCoord in range(9):
                self.squares[((yCoord // 3) * 3) + (xCoord // 3)][((yCoord % 3) * 3) + (xCoord % 3)] = self.rows[yCoord][xCoord]
        consistency = self.board_consistent()
        if not consistency:
            print("This board is not consistent, please reconsider")
            exit()

    def __repr__(self):
        return str(self.rows)

    def print_by_rows(self):
        for row in self.rows:
            print(row)

    def print_by_columns(self):
        for col in self.columns:
            print(col)

    def print_by_squares(self):
        for square in self.squares:
            print(square)

    def row_consistent(self, row_index):
        taken = []
        for element in self.rows[row_index]:
            if element.check_value in taken:
                return False
            else:
                taken.append(element.check_value)
        return True

    def col_consistent(self, col_index):
        taken = []
        for element in self.rows[col_index]:
            if element.check_value in taken:
                return False
            else:
                taken.append(element.check_value)
        return True

    def square_consistent(self, square_index):
        taken = []
        for element in self.squares[square_index]:
            if element.check_value in taken:
                return False
            else:
                taken.append(element.check_value)
        return True

    def board_consistent(self):
        for x in range(9):
            consistent = self.row_consistent(x)
            if not consistent:
                print("row error", x)
                return False
            consistent = self.col_consistent(x)
            if not consistent:
                print("col error", x)
                return False
            consistent = self.square_consistent(x)
            if not consistent:
                print("sqr error", x)
                return False
        print("Board Consistent")
        return True
