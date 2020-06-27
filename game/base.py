class Game:

    def __init__(self, gui=None):
        self.gui = gui

    def start(self):
        if self.gui:
            self.gui.start()
