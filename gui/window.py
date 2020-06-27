from PyQt5.QtWidgets import QMainWindow

from game.indexing.edge import EdgeGrid
from game.indexing.hex import HexGrid
from game.indexing.vertex import VertexGrid
from gui.drawing.base import Drawing, DrawingMixin
from gui.mouse import MouseMixin


class Window(QMainWindow, DrawingMixin, MouseMixin):

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
        self.edge_grid = EdgeGrid()

    @property
    def center(self):
        return self.width() / 2, self.height() / 2

    @property
    def mouse(self):
        return self.mouse_x, self.mouse_y

    def mousePressEvent(self, event):
        if self.handle_vertex_click():
            pass
        elif self.handle_edge_click():
            pass
        else:
            self.handle_hex_click()
        self.update()

    def mouseReleaseEvent(self, event):
        self.click_drawings = []
        self.update()

    def mouseMoveEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()
        self.update()

    def move_drawings(self):
        drawings = []
        if not self.click_drawings and self.mouse_x and self.mouse_y:
            moused_hex = self.moused_hex()
            moused_vertex = self.moused_vertex()
            moused_edge = self.moused_edge()
            if moused_vertex:
                drawings.append(Drawing(self.draw_selected_vertex, [moused_vertex]))
            elif moused_edge:
                drawings.append(Drawing(self.draw_selected_edge, [moused_edge]))
            elif moused_hex:
                drawings.append(Drawing(self.draw_selected_hex, [moused_hex]))
        return drawings

    def paintEvent(self, event):
        for drawing in self.click_drawings + self.move_drawings():
            drawing.apply()
        for hex_ in self.hex_grid.elements:
            self.draw_hex(hex_)
        for vertex in self.vertex_grid.elements:
            self.draw_vertex(vertex)
        for edge in self.edge_grid.elements:
            self.draw_edge(edge)
