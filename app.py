import sys

from game.base import Game

if __name__ == "__main__":
    game = Game(gui=True)
    sys.exit(game.start())
