from gui.drawing.hex import HexDrawingMixin
from gui.drawing.vertex import VertexDrawingMixin


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
):
    pass
