from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPainter, QBrush


class EdgeDrawingMixin:
    EDGE_RADIUS = 10

    def get_edge_center(self, edge):
        return (50, 50)

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
