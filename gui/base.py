from PyQt5.QtWidgets import QApplication

from game.base import Game
from gui.window import Window


class Gui:

    def __init__(self):
        self.app = QApplication([])
        self.window = Window(self, Game())

    def start(self):
        self.app.exec_()
