import os

from .squares import Square, Wall, Guard, Item


class Labyrinth:
    """
        Full Static Object. Need to call build_labyrinth before use. The class
        can be used to know quickely if MacGyver can move in a square or to
        get a square by coords.
    """

    def __init__(self):
        self.maps = {}
        self.rows = 0
        self.columns = 0

        self.build_labyrinth()

    def build_labyrinth(self):
        """
            Docstring
        """

        ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        laby_file = open(os.path.join(ROOT_DIR, 'laby.txt'))

        laby = []

        for line in laby_file:
            row = []
            for s in line:
                if(s != '\n'):
                    row.append(s)
            laby.append(row)

        self.rows = len(laby)
        self.columns = len(laby[0])

        # initialise basic labyrinth
        for i_row, row in enumerate(laby):
            for i_column, square in enumerate(row):
                x = i_column
                y = i_row
                coords = (x, y)

                if(square == 'w'):
                    self.maps[coords] = Wall(coords)
                elif(square == 'g'):
                    self.maps[coords] = Guard(coords)
                elif(square == 'p'):
                    self.maps[coords] = Square(coords)
                    self.gyver_coords = coords
                else:
                    self.maps[coords] = Square(coords)
                    Square.add_square(coords)

        # place itams
        items = [
            {'name': 'Item 1'},
            {'name': 'Item 2'},
            {'name': 'Item 3'},
            {'name': 'Item 4'},
        ]
        for item in items:
            coords = Square.random_pop_square()
            name = item['name']
            self.maps[coords] = Item(coords, name)

        Square.squares = None

    def get_square(self, coords):
        return self.maps[coords]

    def can_move(self, coords):
        square = self.get_square(coords)
        if square is not None:
            can_move = square.can_move()
        else:
            return False

        return can_move
