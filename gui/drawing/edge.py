import math

from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPainter, QBrush

from game.indexing.edge import EdgeGrid
from gui.drawing.hex import HexDrawingMixin


class EdgeDrawingMixin:
    EDGE_RADIUS = 10

    DX_DEdgeCol = math.sqrt(3) * HexDrawingMixin.HEX_RADIUS / 2
    DY_DEdgeCol = 0
    DX_DEdgeRow = - math.sqrt(3) * HexDrawingMixin.HEX_RADIUS / 4
    DY_DEdgeRow = 3 * HexDrawingMixin.HEX_RADIUS / 4

    def get_edge_center(self, edge):
        center_x, center_y = self.center
        center_edge_x = center_x - math.sqrt(3) * HexDrawingMixin.HEX_RADIUS / 4
        center_edge_y = center_y - 3 * HexDrawingMixin.HEX_RADIUS / 4

        d_edge_row = edge.row - EdgeGrid.N_ROWS // 2 + 1
        d_edge_col = edge.col - EdgeGrid.N_COLS // 2 + 1

        dx = EdgeDrawingMixin.DX_DEdgeRow * d_edge_row + EdgeDrawingMixin.DX_DEdgeCol * d_edge_col
        dy = EdgeDrawingMixin.DY_DEdgeRow * d_edge_row + EdgeDrawingMixin.DY_DEdgeCol * d_edge_col

        return center_edge_x + dx, center_edge_y + dy

    def draw_edge(self, edge):
        edge_x, edge_y = self.get_edge_center(edge)
        painter = QPainter(self)
        painter.drawEllipse(
            QPointF(edge_x, edge_y),
            EdgeDrawingMixin.EDGE_RADIUS,
            EdgeDrawingMixin.EDGE_RADIUS
        )

    def draw_selected_edge(self, edge):
        edge_x, edge_y = self.get_edge_center(edge)
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(
            QPointF(edge_x, edge_y),
            EdgeDrawingMixin.EDGE_RADIUS,
            EdgeDrawingMixin.EDGE_RADIUS
        )
