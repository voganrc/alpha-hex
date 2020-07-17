from PyQt5.QtCore import QPointF, Qt

from gui.drawing.base import Drawing


class EdgeMouseMixin:
    def handle_edge_click(self):
        clicked_edge = self.moused_edge()
        if clicked_edge:
            for adjacent_vertex in self.vertex_grid.vertices_for_edge(clicked_edge):
                self.click_drawings.append(Drawing(self.draw_selected_vertex, [adjacent_vertex]))
            self.click_drawings.append(Drawing(self.draw_selected_edge, [clicked_edge]))
            return True
        else:
            return False

    def moused_edge(self):
        for edge in self.edge_grid.elements:
            edge_polygon = self.get_edge_polygon(edge)
            if edge_polygon.containsPoint(QPointF(*self.mouse), Qt.OddEvenFill):
                return edge
        return None
