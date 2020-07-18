from gui.drawing.indexing.edge import EdgeDrawingMixin
from gui.drawing.indexing.hex import HexDrawingMixin
from gui.drawing.indexing.vertex import VertexDrawingMixin


class IndexDrawingMixin(
    HexDrawingMixin,
    VertexDrawingMixin,
    EdgeDrawingMixin,
):
    pass
