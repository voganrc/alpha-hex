from gui.drawing.base import Drawing
from gui.mouse.edge import EdgeMouseMixin
from gui.mouse.hex import HexMouseMixin
from gui.mouse.vertex import VertexMouseMixin


class MouseMixin(
    HexMouseMixin,
    VertexMouseMixin,
    EdgeMouseMixin,
):

    @property
    def mouse(self):
        return self.mouse_x, self.mouse_y

    def mousePressEvent(self, event):
        # if self.handle_vertex_click():
        #     pass
        # elif self.handle_edge_click():
        #     pass
        # else:
        #     self.handle_hex_click()
        self.gui.new_game()
        self.update()

    def mouseReleaseEvent(self, event):
        self.mouse_click_drawings = []
        self.update()

    def mouseMoveEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()
        self.update()

    def mouse_move_drawings(self):
        drawings = []
        if not self.mouse_click_drawings and self.mouse_x and self.mouse_y:
            moused_hex = self.moused_hex()
            moused_vertex = self.moused_vertex()
            moused_edge = self.moused_edge()
            if moused_vertex:
                drawings.append(Drawing(self.draw_selected_vertex, [moused_vertex]))
            elif moused_edge:
                drawings.append(Drawing(self.draw_selected_edge, [moused_edge]))
            elif moused_hex:
                drawings.append(Drawing(self.draw_selected_hex, [moused_hex]))
        return drawings
