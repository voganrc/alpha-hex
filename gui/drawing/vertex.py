import math

from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QPainter, QBrush

from game.indexing.vertex import VertexGrid
from gui.drawing.tile import TILE_RADIUS

VERTEX_RADIUS = 10

DX_DVertexCol = math.sqrt(3) * TILE_RADIUS / 2
DY_DVertexCol = lambda d_col: - TILE_RADIUS / 2 if d_col % 2 == 1 else 0
DX_DVertexRow = - math.sqrt(3) * TILE_RADIUS / 2
DY_DVertexRow = 3 * TILE_RADIUS / 2


def vertex_center(window, vertex):
    center_x, center_y = window.center
    center_vertex_x = center_x - math.sqrt(3) * TILE_RADIUS / 2
    center_vertex_y = center_y - TILE_RADIUS / 2

    d_vertex_row = vertex.row - VertexGrid.N_ROWS // 2 + 1
    d_vertex_col = vertex.col - VertexGrid.N_COLS // 2 + 2

    dx = DX_DVertexRow * d_vertex_row + DX_DVertexCol * d_vertex_col
    dy = DY_DVertexRow * d_vertex_row + DY_DVertexCol(d_vertex_col)

    return center_vertex_x + dx, center_vertex_y + dy


def draw_vertex(window, vertex):
    vertex_x, vertex_y = vertex_center(window, vertex)
    painter = QPainter(window)
    painter.drawEllipse(QPointF(vertex_x, vertex_y), VERTEX_RADIUS, VERTEX_RADIUS)


def draw_selected_vertex(window, vertex):
    vertex_x, vertex_y = vertex_center(window, vertex)
    painter = QPainter(window)
    painter.setBrush(QBrush(Qt.black))
    painter.drawEllipse(QPointF(vertex_x, vertex_y), VERTEX_RADIUS, VERTEX_RADIUS)
