import sys

from game.base import Game
from gui.base import Gui

if __name__ == "__main__":
    game = Game(gui=Gui())
    sys.exit(game.start())
