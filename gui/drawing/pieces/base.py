from gui.drawing.pieces.number import NumberDrawingMixin
from gui.drawing.pieces.road import RoadDrawingMixin
from gui.drawing.pieces.settlement import SettlementDrawingMixin
from gui.drawing.pieces.tile import TileDrawingMixin


class PieceDrawingMixin(
    TileDrawingMixin,
    NumberDrawingMixin,
    SettlementDrawingMixin,
    RoadDrawingMixin,
):
    pass
