from gui.drawing.indexing.edge import EdgeDrawingMixin
from gui.drawing.indexing.hex import HexDrawingMixin
from gui.drawing.indexing.vertex import VertexDrawingMixin


class Drawing:

    def __init__(self, fn, args=None, kwargs=None):
        self.fn = fn
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}

    def apply(self):
        self.fn(*self.args, **self.kwargs)


class DrawingMixin(
    HexDrawingMixin,
    VertexDrawingMixin,
    EdgeDrawingMixin,
):
    pass
