import os

from .gyver import Gyver
from .labyrinth import Labyrinth
from .gameloop import GameLoop
from .drivers import TerminalDriver, PygameDriver

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    labyrinth = Labyrinth()
    gyver = Gyver(labyrinth.gyver_coords)

    #driver = TerminalDriver(gyver=gyver, labyrinth=labyrinth)
    driver = PygameDriver(gyver=gyver, labyrinth=labyrinth, fps=30)

    gameLoop = GameLoop(driver=driver)

    gameLoop.start_loop()
    # gameLoop.end_game()

    return 0


if(__name__ == "__main__"):
    main()

# pipenv install flake8 --dev
# pipenv run flake8
