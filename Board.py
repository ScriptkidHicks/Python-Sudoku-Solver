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

    def set_by_rows(self, input_rows: List[List]):
        self.max = len(input_rows)
        self.rows = [[]] * self.max

        for x in range(len(input_rows)):
            for value in input_rows[x]:
                self.rows[x].append(Tile(value))

        # Now that we have the rows set, we can reference them to build the
        # columns

        self.columns = [[self.rows[x][y] for y in range(self.max)] for x in range(self.max)]
        # Python list comprehension, while slow, rocks

        # This one is a little trickier. Formally the squares are indexed left
        # to right, top to bottom:
        # [[ 1, 2, 3 ]
        #  [ 4, 5, 6 ]
        #  [ 7, 8, 9 ]]

        # this solution is extremely clever, and I am proud of myself
        self.squares = [[None] * 9 ] * 9
        for yCoord in range(9):
            for xCoord in range(9):
                self.squares[((yCoord // 3) * 3) + (xCoord // 3)][((yCoord % 3) * 3) + (xCoord % 3)] = self.rows[yCoord][xCoord]

        consistency = self.board_consistent()
        if not consistency:
            print("This board is not consistent, please check your work")

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
        consistent = True
        for x in range(9):
            consistent = self.row_consistent(x)
            if not consistent:
                return False
            consistent = self.col_consistent(x)
            if not consistent:
                return False
            consistent = self.square_consistent(x)
            if not consistent:
                return False
        return True
