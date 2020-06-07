import numpy as np
from PyQt5.QtCore import QPointF, Qt

from gui.drawing.vertex import VertexDrawingMixin


class MousePositionMixin:

    def moused_vertex(self):
        for vertex in self.vertex_grid.vertices:
            distance = np.linalg.norm(np.array(self.mouse) - np.array(self.get_vertex_center(vertex)))
            if distance < VertexDrawingMixin.VERTEX_RADIUS:
                return vertex
        return None

    def moused_hex(self):
        for hex_ in self.hex_grid.hexes:
            hex_polygon = self.get_hex_polygon(hex_)
            if hex_polygon.containsPoint(QPointF(*self.mouse), Qt.OddEvenFill):
                return hex_
        return None
