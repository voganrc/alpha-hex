from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

from gui.drawing.colors import PLAYER_COLOR_TO_RGB
from gui.drawing.polygons import settlement_polygon


class SettlementDrawingMixin:

    def get_settlement_center(self, settlement):
        return self.get_vertex_center(settlement.vertex)

    def get_settlement_polygon(self, settlement):
        return settlement_polygon(*self.get_settlement_center(settlement), 40)

    def draw_settlement(self, settlement):
        polygon = self.get_settlement_polygon(settlement)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(*PLAYER_COLOR_TO_RGB[settlement.player.color])))
        painter.drawPolygon(polygon)
