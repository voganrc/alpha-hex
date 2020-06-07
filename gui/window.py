from PyQt5.QtWidgets import QMainWindow

from game.indexing.hex import HexGrid
from game.indexing.vertex import VertexGrid
from gui.drawing.base import Drawing, DrawingMixin
from gui.mouse import MousePositionMixin


class Window(QMainWindow, DrawingMixin, MousePositionMixin):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semaphores of Catan")
        self.showMaximized()

        self.setMouseTracking(True)
        self.mouse_x = None
        self.mouse_y = None

        self.drawings = []

        self.hex_grid = HexGrid()
        self.vertex_grid = VertexGrid()

    @property
    def center(self):
        return self.width() / 2, self.height() / 2

    @property
    def mouse(self):
        return self.mouse_x, self.mouse_y

    def mouseMoveEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()

        moused_vertex = self.moused_vertex()
        moused_hex = self.moused_hex()

        if moused_vertex:
            self.drawings.append(Drawing(self.draw_selected_vertex, [moused_vertex]))
        elif moused_hex:
            self.drawings.append(Drawing(self.draw_selected_hex, [moused_hex]))

        self.update()

    def paintEvent(self, event):
        for draw_task in self.drawings:
            draw_task.apply()
        self.drawings = []

        for hex_ in self.hex_grid.hexes:
            self.draw_hex(hex_)
        for vertex in self.vertex_grid.vertices:
            self.draw_vertex(vertex)
