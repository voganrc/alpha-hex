from gui.base import Gui


class Game:

    def __init__(self, attach_gui=True):
        self.gui = None
        if attach_gui:
            self.gui = Gui()

    def start(self):
        if self.gui:
            self.gui.start()
