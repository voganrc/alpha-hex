from PyQt5.QtWidgets import QApplication

from gui.window import Window


class Gui:

    def __init__(self):
        self.application = QApplication([])
        self.window = Window()

    def start(self):
        self.application.exec()
