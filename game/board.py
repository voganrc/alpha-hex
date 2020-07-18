import itertools
import random

from game.indexing.edge import EdgeGrid
from game.indexing.hex import HexGrid
from game.indexing.vertex import VertexGrid
from game.phase import Phase
from game.pieces.tile import Tile, DesertTile


class Board:
    DEFAULT_NUMBER_ORDER = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

    def __init__(self):
        self.hex_grid = HexGrid()
        self.vertex_grid = VertexGrid()
        self.edge_grid = EdgeGrid()

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
                hex_.tile.number = None
            else:
                hex_.tile.number = Board.DEFAULT_NUMBER_ORDER[number_idx]
                number_idx += 1

    def legal_vertices(self, player, phase):
        if phase == Phase.SET_UP:
            illegal_vertices = set()
            for vertex in self.vertex_grid.elements:
                if vertex.building:
                    illegal_vertices.update(self.neighbors(vertex))
            legal_vertices = set(self.vertex_grid.elements).difference(illegal_vertices)
            return VertexGrid.sort(legal_vertices)

        else:
            raise NotImplementedError

    def neighbors(self, vertex):
        return set(itertools.chain.from_iterable(
            self.vertex_grid.vertices_for_edge(edge)
            for edge in self.edge_grid.edges_for_vertex(vertex)
        ))
