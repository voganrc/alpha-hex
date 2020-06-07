from PyQt5.QtWidgets import QMainWindow

from game.indexing.hex import HexGrid
from game.indexing.vertex import VertexGrid
from gui.drawing.base import DrawTask
from gui.drawing.hex import draw_hex
from gui.drawing.vertex import draw_vertex, draw_selected_vertex
from gui.mouse import moused_vertices


class FieldTile(object):
    pass


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semaphores of Catan")
        self.showMaximized()
        self.mouse_x = None
        self.mouse_y = None
        self.setMouseTracking(True)
        self.vertex_grid = VertexGrid()
        self.draw_tasks = []

    @property
    def center(self):
        return self.width() / 2, self.height() / 2

    def mouseMoveEvent(self, event):
        # print("movement")
        # painter = QPainter(self)
        # painter.drawText(200, 200, str((event.x(), event.y())))
        pass

    def mouseMoveEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()
        vertices = moused_vertices(self, self.vertex_grid)
        for vertex in vertices:
            self.draw_tasks.append(DrawTask(draw_selected_vertex, [self, vertex]))
        self.update()

    def paintEvent(self, event):
        for draw_task in self.draw_tasks:
            draw_task.apply()
        self.draw_tasks = []

        hex_grid = HexGrid()
        for hex_ in hex_grid.hexes:
            draw_hex(self, hex_)
        for vertex in self.vertex_grid.vertices:
            draw_vertex(self, vertex)
