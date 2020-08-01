import itertools
import random
from collections import defaultdict

from game.indexing.edge import EdgeGrid
from game.indexing.hex import HexGrid
from game.indexing.vertex import VertexGrid
from game.phase import Phase
from game.pieces.tile import Tile, DesertTile


class Board:
    DEFAULT_NUMBER_ORDER = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

    def __init__(self, game):
        self.game = game
        self.hex_grid = HexGrid()
        self.vertex_grid = VertexGrid()
        self.edge_grid = EdgeGrid()
        self.hexes_for_number = defaultdict(list)

        tile_order = []
        for tile_cls in Tile.__subclasses__():
            tile_order += [tile_cls] * tile_cls.COUNT
        random.shuffle(tile_order)

        for hex_, tile_cls in zip(self.hex_grid.elements, tile_order):
            hex_.tile = tile_cls(hex_)

        number_idx = 0
        spiral_traversal = self.hex_grid.spiral_traversal()
        for hex_ in spiral_traversal:
            if isinstance(hex_.tile, DesertTile):
                hex_.number = 7
            else:
                hex_.number = Board.DEFAULT_NUMBER_ORDER[number_idx]
                number_idx += 1
            self.hexes_for_number[hex_.number].append(hex_)

    def handle_roll(self, dice_sum):
        activated_hexes = self.hexes_for_number[dice_sum]
        for activated_hex in activated_hexes:
            activated_vertices = self.vertex_grid.vertices_for_hex(activated_hex)
            activated_buildings = [vertex.building for vertex in activated_vertices if vertex.building]
            map(lambda building: building.pay(activated_hex.tile.RESOURCE), activated_buildings)

    def legal_vertices(self, player):
        if self.game.phase == Phase.SET_UP:
            legal_vertex_set = self._vertices_with_no_adjacent_settlements()
        else:
            legal_vertex_set = self._vertices_with_no_adjacent_settlements() & self._vertices_connected_to_roads(player)
        return VertexGrid.sort(legal_vertex_set)

    def legal_edges(self, player):
        legal_edges = []
        accessible_vertices = set(
            vertex for vertex in self._vertices_connected_to_roads(player)
            if vertex.building is None or vertex.building.player == player
        )
        for edge in self.edge_grid.elements:
            if edge.road is None:
                adjacent_vertices = self.vertex_grid.vertices_for_edge(edge)
                if any(vertex in accessible_vertices for vertex in adjacent_vertices):
                    legal_edges.append(edge)
        return legal_edges

    def _vertices_with_no_adjacent_settlements(self):
        illegal_vertices = set()
        for vertex in self.vertex_grid.elements:
            if vertex.building is not None:
                illegal_vertices.update(self._vertex_neighborhood(vertex))
        legal_vertices = set(self.vertex_grid.elements) - illegal_vertices
        return legal_vertices

    def _vertices_connected_to_roads(self, player):
        owned_edges = [edge for edge in self.edge_grid.elements if edge.road and edge.road.player == player]
        return set(itertools.chain.from_iterable(
            self.vertex_grid.vertices_for_edge(edge) for edge in owned_edges
        ))

    def _vertex_neighborhood(self, center_vertex):
        return set(itertools.chain.from_iterable(
            self.vertex_grid.vertices_for_edge(edge)
            for edge in self.edge_grid.edges_for_vertex(center_vertex)
        ))
