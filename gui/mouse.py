import numpy as np
from PyQt5.QtCore import QPointF, Qt

from gui.drawing.base import Drawing
from gui.drawing.edge import EdgeDrawingMixin
from gui.drawing.vertex import VertexDrawingMixin


class MouseMixin:

    def handle_hex_click(self):
        clicked_hex = self.moused_hex()
        if clicked_hex:
            self.click_drawings.append(Drawing(self.draw_selected_hex, [clicked_hex]))
            for adjacent_vertex in self.vertex_grid.vertices_for_hex(clicked_hex):
                self.click_drawings.append(Drawing(self.draw_selected_vertex, [adjacent_vertex]))
            return True
        else:
            return False

    def moused_hex(self):
        for hex_ in self.hex_grid.elements:
            hex_polygon = self.get_hex_polygon(hex_)
            if hex_polygon.containsPoint(QPointF(*self.mouse), Qt.OddEvenFill):
                return hex_
        return None

    def handle_vertex_click(self):
        clicked_vertex = self.moused_vertex()
        if clicked_vertex:
            for adjacent_hex in self.hex_grid.hexes_for_vertex(clicked_vertex):
                self.click_drawings.append(Drawing(self.draw_selected_hex, [adjacent_hex]))
            for adjacent_edge in self.edge_grid.edges_for_vertex(clicked_vertex):
                self.click_drawings.append(Drawing(self.draw_selected_edge, [adjacent_edge]))
            self.click_drawings.append(Drawing(self.draw_selected_vertex, [clicked_vertex]))
            return True
        else:
            return False

    def moused_vertex(self):
        for vertex in self.vertex_grid.elements:
            distance = np.linalg.norm(np.array(self.mouse) - np.array(self.get_vertex_center(vertex)))
            if distance < VertexDrawingMixin.VERTEX_RADIUS:
                return vertex
        return None

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
            distance = np.linalg.norm(np.array(self.mouse) - np.array(self.get_edge_center(edge)))
            if distance < EdgeDrawingMixin.EDGE_RADIUS:
                return edge
        return None
