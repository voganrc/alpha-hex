from PyQt5.QtWidgets import QApplication

from game.base import Game
from gui.window import Window


class Gui:

    def __init__(self):
        self.application = QApplication([])
        self.window = Window(self)

    def new_game(self):
        self.window.game = Game()

    def start(self):
        self.application.exec()
