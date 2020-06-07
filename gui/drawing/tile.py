from PyQt5.QtGui import QPainter, QBrush, QColor

from game.tile import FieldsTile, HillsTile, ForestTile, MountainsTile, PastureTile, DesertTile
from gui.drawing.polygons import regular_polygon

TILE_RADIUS = 100
TILE_ROTATION = 90

TILE_TO_RGB = {
    HillsTile: (193, 67, 55),
    ForestTile: (39, 110, 52),
    MountainsTile: (181, 182, 184),
    FieldsTile: (254, 215, 59),
    PastureTile: (159, 199, 70),
    DesertTile: (248, 199, 96),
}


def draw_tile(window, tile):
    hexagon = regular_polygon(6, 500, 500, TILE_RADIUS, TILE_ROTATION)
    r, g, b = TILE_TO_RGB[tile.__class__]

    painter = QPainter(window)
    painter.setBrush(QBrush(QColor(r, g, b)))
    painter.drawPolygon(hexagon)
