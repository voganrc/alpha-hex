import math

from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPainter, QBrush

from game.indexing.vertex import VertexGrid
from gui.drawing.tile import TILE_RADIUS


class VertexDrawingMixin:
    DX_DVertexCol = math.sqrt(3) * TILE_RADIUS / 2
    DY_DVertexCol = lambda d_col: - TILE_RADIUS / 2 if d_col % 2 == 1 else 0
    DX_DVertexRow = - math.sqrt(3) * TILE_RADIUS / 2
    DY_DVertexRow = 3 * TILE_RADIUS / 2

    VERTEX_RADIUS = 10

    def get_vertex_center(self, vertex):
        center_x, center_y = self.center
        center_vertex_x = center_x - math.sqrt(3) * TILE_RADIUS / 2
        center_vertex_y = center_y - TILE_RADIUS / 2

        d_vertex_row = vertex.row - VertexGrid.N_ROWS // 2 + 1
        d_vertex_col = vertex.col - VertexGrid.N_COLS // 2 + 2

        dx = VertexDrawingMixin.DX_DVertexRow * d_vertex_row + VertexDrawingMixin.DX_DVertexCol * d_vertex_col
        dy = VertexDrawingMixin.DY_DVertexRow * d_vertex_row + VertexDrawingMixin.DY_DVertexCol(d_vertex_col)

        return center_vertex_x + dx, center_vertex_y + dy

    def draw_vertex(self, vertex):
        vertex_x, vertex_y = self.get_vertex_center(vertex)
        painter = QPainter(self)
        painter.drawEllipse(
            QPointF(vertex_x, vertex_y),
            VertexDrawingMixin.VERTEX_RADIUS,
            VertexDrawingMixin.VERTEX_RADIUS
        )

    def draw_selected_vertex(self, vertex):
        vertex_x, vertex_y = self.get_vertex_center(vertex)
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(
            QPointF(vertex_x, vertex_y),
            VertexDrawingMixin.VERTEX_RADIUS,
            VertexDrawingMixin.VERTEX_RADIUS,
        )
