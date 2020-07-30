from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow

from game.base import Game
from game.phase import Phase
from gui.drawing.base import DrawingMixin
from gui.mouse.base import MouseMixin


class Window(QMainWindow, DrawingMixin, MouseMixin):
    MOVE_INTERVAL_MS = 30

    def __init__(self, gui, game):
        super().__init__()

        self.gui = gui
        self.game = game

        self.setWindowTitle("Semaphores of Catan")
        self.showMaximized()

        self.setMouseTracking(True)
        self.mouse_x = None
        self.mouse_y = None
        self.mouse_click_drawings = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.advance)
        self.timer.start(Window.MOVE_INTERVAL_MS)

    @property
    def center(self):
        return self.width() / 2, self.height() / 2

    def advance(self):
        self.game.advance()
        self.update()
        if self.game.phase == Phase.COMPLETED:
            self.game = Game()

    def paintEvent(self, event):
        # for drawing in self.mouse_click_drawings + self.mouse_move_drawings():
        #     drawing.apply()
        # for vertex in self.game.board.vertex_grid.elements:
        #     self.draw_vertex(vertex)
        # for edge in self.game.board.edge_grid.elements:
        #     self.draw_edge(edge)
        self.draw_board()
