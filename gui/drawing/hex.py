import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush

from game.indexing.hex import HexGrid
from gui.drawing.polygons import regular_polygon
from gui.drawing.tile import TILE_RADIUS, TILE_ROTATION


class HexDrawingMixin:
    DX_DHexCol = math.sqrt(3) * TILE_RADIUS
    DY_DHexCol = 0
    DX_DHexRow = - DX_DHexCol / 2
    DY_DHexRow = 1.5 * TILE_RADIUS

    def get_hex_center(self, hex_):
        center_x, center_y = self.center

        d_hex_row = hex_.row - HexGrid.N_ROWS // 2
        d_hex_col = hex_.col - HexGrid.N_COLS // 2

        dx = HexDrawingMixin.DX_DHexRow * d_hex_row + HexDrawingMixin.DX_DHexCol * d_hex_col
        dy = HexDrawingMixin.DY_DHexRow * d_hex_row + HexDrawingMixin.DY_DHexCol * d_hex_col

        return center_x + dx, center_y + dy

    def get_hex_polygon(self, hex_):
        hex_x, hex_y = self.get_hex_center(hex_)
        return regular_polygon(n_sides=6, x=hex_x, y=hex_y, radius=TILE_RADIUS, theta_0=TILE_ROTATION)

    def draw_hex(self, hex_):
        hexagon = self.get_hex_polygon(hex_)
        painter = QPainter(self)
        painter.drawPolygon(hexagon)

    def draw_selected_hex(self, hex_):
        hexagon = self.get_hex_polygon(hex_)
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.gray))
        painter.drawPolygon(hexagon)
