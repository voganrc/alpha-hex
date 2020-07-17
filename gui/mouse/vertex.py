from pandas.tests.extension.numpy_.test_numpy_nested import np

from gui.drawing.base import Drawing
from gui.drawing.vertex import VertexDrawingMixin


class VertexMouseMixin:
    def handle_vertex_click(self):
        clicked_vertex = self.moused_vertex()
        if clicked_vertex:
            for adjacent_hex in self.game.board.hex_grid.hexes_for_vertex(clicked_vertex):
                self.mouse_click_drawings.append(Drawing(self.draw_selected_hex, [adjacent_hex]))
            for adjacent_edge in self.game.board.edge_grid.edges_for_vertex(clicked_vertex):
                self.mouse_click_drawings.append(Drawing(self.draw_selected_edge, [adjacent_edge]))
            self.mouse_click_drawings.append(Drawing(self.draw_selected_vertex, [clicked_vertex]))
            return True
        else:
            return False

    def moused_vertex(self):
        for vertex in self.game.board.vertex_grid.elements:
            distance = np.linalg.norm(np.array(self.mouse) - np.array(self.get_vertex_center(vertex)))
            if distance < VertexDrawingMixin.VERTEX_RADIUS:
                return vertex
        return None
