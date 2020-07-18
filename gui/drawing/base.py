from PyQt5.QtGui import QColor

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

    def draw_water(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(*DrawingMixin.WATER_RGB))
        self.setPalette(p)
