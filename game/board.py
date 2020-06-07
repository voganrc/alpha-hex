from tile import Tile
from tile import DesertTile
import random
from typing import List
from enum import Enum
from tile import Vertex


#  Physical         Grid
#   Board          Mapping
# -------------------------
#   a b c         a b c . .
#  d e f g        d e f g .
# h i j k l  -->  h i j k l
#  m n o p        . m n o p
#   q r s         . . q r s


class TilePlacement(Enum):
    BEGINNER = 0
    RANDOM = 1


class NumberPlacement(Enum):
    BEGINNER = 0
    SORTED = 1
    RANDOM = 2


class HarborPlacement(Enum):
    BEGINNER = 0
    FRAME = 1
    RANDOM = 2


class Board:

    HEX_RADIUS = 2
    GRID_LENGTH = HEX_RADIUS * 2 + 1

    CORNER_GRID_COORDS = [
        (0, 0),
        (0, HEX_RADIUS),
        (HEX_RADIUS, 0),
        (HEX_RADIUS, 2 * HEX_RADIUS),
        (2 * HEX_RADIUS, HEX_RADIUS),
        (2 * HEX_RADIUS, 2 * HEX_RADIUS),
    ]

    CCW_GRID_DIRECTIONS = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
    ]

    DEFAULT_NUMBER_ORDER = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

    def __init__(self):

        self.grid = [
            [None for i in range(Board.GRID_LENGTH)]
            for j in range(Board.GRID_LENGTH)
        ]

        tile_order = []
        for tile_cls in Tile.__subclasses__():
            tile_order += [tile_cls] * tile_cls.COUNT
        random.shuffle(tile_order)

        grid_order = []
        for grid_row in range(Board.GRID_LENGTH):
            for grid_col in range(Board.GRID_LENGTH):
                grid_diag = grid_col - grid_row
                if abs(grid_diag) <= Board.HEX_RADIUS: 
                    grid_order.append((grid_row, grid_col))
        random.shuffle(grid_order)

        for tile_cls, (grid_row, grid_col) in zip(tile_order, grid_order):
            hex_x, hex_y = Board.grid_to_hex(grid_row, grid_col)
            self.grid[grid_row][grid_col] = tile_cls(hex_x, hex_y)


        traversal = Board.spiral_traversal(Board.HEX_RADIUS)
        number_idx = 0
        for (grid_row, grid_col) in traversal:
            tile = self.grid[grid_row][grid_col]
            if isinstance(tile, DesertTile):
                tile.number = None
            else:
                tile.number = Board.DEFAULT_NUMBER_ORDER[number_idx]
                number_idx += 1

        self.vertices = []
        for grid_row in range(Board.GRID_LENGTH):
            for grid_col in range(Board.GRID_LENGTH):
                tile = self.grid[grid_row][grid_col]
                if tile is None:
                    continue

                if not tile.nw_vertex:
                    new_vertex = Vertex()
                    self.vertices.append(new_vertex)

                    tile.nw_vertex = new_vertex
                    new_vertex.se_tile = tile
                    
                    w_tile = self.get_relative_tile(grid_row, grid_col, 0, -1)
                    if w_tile:
                        w_tile.ne_vertex = new_vertex
                        new_vertex.sw_tile = w_tile

                    nw_tile = self.get_relative_tile(grid_row, grid_col, -1, -1)
                    if nw_tile:
                        nw_tile.s_vertex = new_vertex
                        new_vertex.n_tile = nw_tile

                if not tile.n_vertex:
                    new_vertex = Vertex()
                    self.vertices.append(new_vertex)

                    tile.n_vertex = new_vertex
                    new_vertex.s_tile = tile
                    
                    ne_tile = self.get_relative_tile(grid_row, grid_col, -1, 0)
                    if ne_tile:
                        ne_tile.sw_vertex = new_vertex
                        new_vertex.ne_tile = ne_tile

                    nw_tile = self.get_relative_tile(grid_row, grid_col, -1, -1)
                    if nw_tile:
                        nw_tile.se_vertex = new_vertex
                        new_vertex.nw_tile = nw_tile

                if not tile.ne_vertex:
                    new_vertex = Vertex()
                    self.vertices.append(new_vertex)

                    tile.ne_vertex = new_vertex
                    new_vertex.sw_tile = tile
                    
                    ne_tile = self.get_relative_tile(grid_row, grid_col, -1, 0)
                    if ne_tile:
                        ne_tile.s_vertex = new_vertex
                        new_vertex.n_tile = ne_tile

                    e_tile = self.get_relative_tile(grid_row, grid_col, 0, 1)
                    if e_tile:
                        e_tile.nw_vertex = new_vertex
                        new_vertex.se_tile = e_tile

        done = False
        while not done:

            done = True

            settled = random.sample(self.vertices, 8)
            for vertex in settled:
                vertex.building = True

            for grid_row in range(Board.GRID_LENGTH):
                for grid_col in range(Board.GRID_LENGTH):
                    tile = self.grid[grid_row][grid_col]
                    if tile is None:
                        continue

                    if tile.n_vertex and tile.ne_vertex and tile.n_vertex.building and tile.ne_vertex.building:
                        done = False
                    if tile.ne_vertex and tile.se_vertex and tile.ne_vertex.building and tile.se_vertex.building:
                        done = False
                    if tile.se_vertex and tile.s_vertex and tile.se_vertex.building and tile.s_vertex.building:
                        done = False
                    if tile.s_vertex and tile.sw_vertex and tile.s_vertex.building and tile.sw_vertex.building:
                        done = False
                    if tile.sw_vertex and tile.nw_vertex and tile.sw_vertex.building and tile.nw_vertex.building:
                        done = False
                    if tile.nw_vertex and tile.n_vertex and tile.nw_vertex.building and tile.n_vertex.building:
                        done = False

            if not done:
                for vertex in settled:
                    vertex.building = False



    def get_relative_tile(self, row, col, d_row, d_col):
        new_row = row + d_row
        if new_row < 0 or new_row >= Board.GRID_LENGTH:
            return None

        new_col = col + d_col
        if new_col < 0 or new_col >= Board.GRID_LENGTH:
            return None

        return self.grid[new_row][new_col]

    @classmethod
    def grid_to_hex(cls, grid_row, grid_col):
        hex_x = grid_col - cls.HEX_RADIUS
        hex_y = cls.HEX_RADIUS - grid_row
        return (hex_x, hex_y)


    @classmethod
    def spiral_traversal(cls, hex_radius) -> List[Tile]:
        if hex_radius < 0:
            return []

        start_row, start_col = [cls.GRID_LENGTH // 2 - hex_radius] * 2
        traversal = [(start_row, start_col)]

        for direction in cls.CCW_GRID_DIRECTIONS:
            d_row, d_col = direction
            for i in range(hex_radius):
                prev_row, prev_col = traversal[-1]
                traversal.append((prev_row + d_row, prev_col + d_col))

        if hex_radius > 0:
            del traversal[-1]

        return traversal + cls.spiral_traversal(hex_radius - 1)
