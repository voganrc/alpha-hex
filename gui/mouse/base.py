from gui.mouse.edge import EdgeMouseMixin
from gui.mouse.hex import HexMouseMixin
from gui.mouse.vertex import VertexMouseMixin


class MouseMixin(
    HexMouseMixin,
    VertexMouseMixin,
    EdgeMouseMixin,
):
    pass
