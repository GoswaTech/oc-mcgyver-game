class Gyver:
    """Full Static Object, here we move the player with move() function.

    Before using this class, we need to initialise it with init_gyver.
    """

    def __init__(self, gyver_coords):
        """
            coords = (x, y)
        """
        self.coords = gyver_coords
        self.win = False
        self.lose = False
        self.items = {}

    def move(self, labyrinth, **kwargs):
        """You can move the player with the simple method
        move(x=<int:optional>, y=<int:optional>).

        This method verify if gyver can move in the labyrinth and return
        the current square.
        """
        x = kwargs.pop('x', 0)
        y = kwargs.pop('y', 0)

        coords = (self.coords[0]+x, self.coords[1]+y)

        if(labyrinth.can_move(coords)):
            self.coords = coords

        return labyrinth.get_square(self.coords)

    def set_win(self):
        self.win = True

    def set_lose(self):
        self.lose = True

    def add_item(self, name):
        self.items[name] = True
