from gui.drawing.pieces.settlement import SettlementDrawingMixin
from gui.drawing.pieces.tile import TileDrawingMixin


class PieceDrawingMixin(
    TileDrawingMixin,
    SettlementDrawingMixin,
):
    pass
