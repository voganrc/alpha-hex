from PyQt5.QtWidgets import QApplication

from gui.window import Window


class Gui:

    def __init__(self, game):
        self.application = QApplication([])
        self.window = Window(game)

    def start(self):
        self.application.exec()
