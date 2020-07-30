from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

from gui.drawing.colors import PLAYER_COLOR_TO_RGB


class RoadDrawingMixin:

    def get_road_center(self, road):
        return self.get_edge_center(road.edge)

    def get_road_polygon(self, road):
        return self.get_edge_polygon(road.edge)

    def draw_road(self, road):
        polygon = self.get_road_polygon(road)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(*PLAYER_COLOR_TO_RGB[road.player.color])))
        painter.drawPolygon(polygon)
