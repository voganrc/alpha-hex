import sys

from gui.base import Gui

if __name__ == "__main__":
    gui = Gui()
    gui.new_game()
    sys.exit(gui.start())
