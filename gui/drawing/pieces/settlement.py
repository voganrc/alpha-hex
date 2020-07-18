from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

from game.player.base import Player
from gui.drawing.polygons import settlement_polygon


class SettlementDrawingMixin:
    PLAYER_TO_RGB = {
        Player.RED: (255, 0, 0),
        Player.BLUE: (0, 0, 255),
        Player.WHITE: (255, 255, 255),
        Player.ORANGE: (255, 165, 0),
    }

    def get_settlement_center(self, settlement):
        return self.get_vertex_center(settlement.vertex)

    def get_settlement_polygon(self, settlement):
        return settlement_polygon(*self.get_settlement_center(settlement), 40)

    def draw_settlement(self, settlement):
        polygon = self.get_settlement_polygon(settlement)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(*SettlementDrawingMixin.PLAYER_TO_RGB[settlement.player])))
        painter.drawPolygon(polygon)
