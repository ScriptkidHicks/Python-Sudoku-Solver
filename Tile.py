"""This is the tile object. It's a neat way for us to reference the same number
in multiple places without getting too messy about it. We will use this to
build lists of columns, rows, and squares. It conforms well to Python's object
oriented style, and it will allow us to scale up to a 4x4 table, or even a 3
dimensional version if necessary."""


class Tile:
    """This object is pretty simple, but a useful base piece"""

    def __init__(self, initial_value=None, max=9):
        self.value = None if initial_value == 0 else initial_value
        self.solved = False
        self.possibles = [x for x in range(max)]
        if self.value is not None:
            self.possibles = [self.value]
            self.solved = True

    def set_value(self, new_value):
        self.value = new_value
        self.possibles = [self.value]
        self.solved = True

    def check_value(self):
        return self.value

    def check_possibles(self):
        return self.possibles

    def eliminate_possible(self, value):
        changed = False
        if value in self.possibles:
            self.possibles.remove(value)
            changed = True
        if len(self.possibles) == 1:
            self.value = self.possibles[0]
            self.solved = True
            return "solved", changed
        if len(self.possibles) == 0:
            return "error", changed
        else:
            return "unsolved", changed

    def __repr__(self):
        return str(self.value)