from game.board import Board
from gui.base import Gui


class Game:

    def __init__(self, gui=False):
        self.board = Board()
        if gui:
            self.gui = Gui(self)

    def start(self):
        if self.gui:
            self.gui.start()
