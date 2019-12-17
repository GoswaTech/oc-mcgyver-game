from random import random


class Square:
    """A Square is an Area where Mac Gyver can move or not."""

    squares = []

    def __init__(self, coords):
        """
            coords = (x, y)
        """
        self.coords = coords
        self.type = 'Floor'

    def can_move(self):
        """True if Mac Gyver can move on it.

        False is he can't.
        """
        return True

    def after_move(self, **kwargs):
        """Execute method(s) after a move."""
        return 0

    def get_type(self):
        return self.type

    def add_square(key):
        Square.squares.append(key)

    def random_pop_square():
        rand_int = int(random()*(len(Square.squares)-1))

        return Square.squares.pop(rand_int)


class Wall(Square):
    """The Wall block MacGyver's moves."""

    def __init__(self, coords):
        super().__init__(coords)
        self.type = "Wall"

    def can_move(self):
        return False


class Item(Square):
    """Item is a win condition.

    When MacGyver is on, it become a simple Square.
    """

    def __init__(self, coords, name):
        super().__init__(coords)
        self.type = name
        self.taken = False

    def after_move(self, **kwargs):
        gyver = kwargs.pop('gyver', None)
        if gyver is not None:
            gyver.add_item(self.type)
            self.taken = True

    def get_type(self):
        return 'Floor' if self.taken else self.type


class Guard(Square):
    """Guard kill MacGyver if all items are not on his hand, else the Guard
    die."""

    def __init__(self, coords):
        super().__init__(coords)
        self.type = "Guard"

    def after_move(self, **kwargs):
        gyver = kwargs.pop('gyver', None)
        if gyver is not None:

            if(len(gyver.items) == 4):
                gyver.set_win()
            else:
                gyver.set_lose()
