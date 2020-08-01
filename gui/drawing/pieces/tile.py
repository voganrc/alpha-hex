from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen

from game.pieces.tile import HillsTile, ForestTile, MountainsTile, FieldsTile, PastureTile, DesertTile


class TileDrawingMixin:
    TILE_CLS_TO_RGB = {
        HillsTile: (221, 86, 36),
        ForestTile: (15, 145, 61),
        MountainsTile: (154, 160, 137),
        FieldsTile: (237, 180, 17),
        PastureTile: (135, 180, 16),
        DesertTile: (199, 171, 116),
    }

    def get_tile_center(self, tile):
        return self.get_hex_center(tile.hex_)

    def get_tile_polygon(self, tile):
        return self.get_hex_polygon(tile.hex_)

    def draw_tile(self, tile):
        hexagon = self.get_tile_polygon(tile)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(*TileDrawingMixin.TILE_CLS_TO_RGB[tile.__class__])))
        painter.drawPolygon(hexagon)
