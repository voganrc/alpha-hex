from PyQt5.QtGui import QColor

from game.pieces.settlement import Settlement
from gui.drawing.indexing.base import IndexDrawingMixin
from gui.drawing.pieces.base import PieceDrawingMixin


class Drawing:

    def __init__(self, fn, args=None, kwargs=None):
        self.fn = fn
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}

    def apply(self):
        self.fn(*self.args, **self.kwargs)


class DrawingMixin(
    IndexDrawingMixin,
    PieceDrawingMixin,
):
    WATER_RGB = (81, 182, 232)

    def draw_board(self):
        self.draw_water()
        for hex_ in self.game.board.hex_grid.elements:
            self.draw_tile(hex_.tile)
        for edge in self.game.board.edge_grid.elements:
            if edge.road:
                self.draw_road(edge.road)
        for vertex in self.game.board.vertex_grid.elements:
            if vertex.building and isinstance(vertex.building, Settlement):
                self.draw_settlement(vertex.building)

    def draw_water(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(*DrawingMixin.WATER_RGB))
        self.setPalette(p)
