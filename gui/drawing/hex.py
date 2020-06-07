import math

from PyQt5.QtGui import QPainter

from game.indexing.hex import HexGrid
from gui.drawing.polygons import regular_polygon
from gui.drawing.tile import TILE_RADIUS, TILE_ROTATION

DX_DHexCol = math.sqrt(3) * TILE_RADIUS
DY_DHexCol = 0
DX_DHexRow = - DX_DHexCol / 2
DY_DHexRow = 1.5 * TILE_RADIUS


def hex_center(window, hex_):
    center_x, center_y = window.center

    d_hex_row = hex_.row - HexGrid.N_ROWS // 2
    d_hex_col = hex_.col - HexGrid.N_COLS // 2

    dx = DX_DHexRow * d_hex_row + DX_DHexCol * d_hex_col
    dy = DY_DHexRow * d_hex_row + DY_DHexCol * d_hex_col

    return center_x + dx, center_y + dy


def draw_hex(window, hex_):
    hex_x, hex_y = hex_center(window, hex_)

    hexagon = regular_polygon(n_sides=6, x=hex_x, y=hex_y, radius=TILE_RADIUS, theta_0=TILE_ROTATION)

    painter = QPainter(window)
    painter.drawPolygon(hexagon)
