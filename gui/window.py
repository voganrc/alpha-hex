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

        self.click_drawings = []

        self.hex_grid = HexGrid()
        self.vertex_grid = VertexGrid()

    @property
    def center(self):
        return self.width() / 2, self.height() / 2

    @property
    def mouse(self):
        return self.mouse_x, self.mouse_y

    def mousePressEvent(self, event):
        clicked_vertex = self.moused_vertex()
        clicked_hex = self.moused_hex()
        if clicked_vertex:
            for adjacent_hex in self.hex_grid.hexes_for_vertex(clicked_vertex):
                self.click_drawings.append(Drawing(self.draw_selected_hex, [adjacent_hex]))
            self.click_drawings.append(Drawing(self.draw_selected_vertex, [clicked_vertex]))
        elif clicked_hex:
            self.click_drawings.append(Drawing(self.draw_selected_hex, [clicked_hex]))
            for adjacent_vertex in self.vertex_grid.vertices_for_hex(clicked_hex):
                self.click_drawings.append(Drawing(self.draw_selected_vertex, [adjacent_vertex]))
        self.update()

    def mouseReleaseEvent(self, event):
        self.click_drawings = []
        self.update()

    def mouseMoveEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()
        self.update()

    def paintEvent(self, event):
        for drawing in self.click_drawings + self.move_drawings():
            drawing.apply()
        for hex_ in self.hex_grid.hexes:
            self.draw_hex(hex_)
        for vertex in self.vertex_grid.vertices:
            self.draw_vertex(vertex)

    def move_drawings(self):
        drawings = []
        if not self.click_drawings and self.mouse_x and self.mouse_y:
            moused_vertex = self.moused_vertex()
            moused_hex = self.moused_hex()
            if moused_vertex:
                drawings.append(Drawing(self.draw_selected_vertex, [moused_vertex]))
            elif moused_hex:
                drawings.append(Drawing(self.draw_selected_hex, [moused_hex]))
        return drawings
