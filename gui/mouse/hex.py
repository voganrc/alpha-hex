from PyQt5.QtCore import QPointF, Qt

from gui.drawing.base import Drawing


class HexMouseMixin:
    def handle_hex_click(self):
        clicked_hex = self.moused_hex()
        if clicked_hex:
            self.mouse_click_drawings.append(Drawing(self.draw_selected_hex, [clicked_hex]))
            for adjacent_vertex in self.game.board.vertex_grid.vertices_for_hex(clicked_hex):
                self.mouse_click_drawings.append(Drawing(self.draw_selected_vertex, [adjacent_vertex]))
            return True
        else:
            return False

    def moused_hex(self):
        for hex_ in self.game.board.hex_grid.elements:
            hex_polygon = self.get_hex_polygon(hex_)
            if hex_polygon.containsPoint(QPointF(*self.mouse), Qt.OddEvenFill):
                return hex_
        return None
