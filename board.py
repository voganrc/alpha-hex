from tile import Tile
from tile import DesertTile
import random
from typing import List
from enum import Enum


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
    GRID_SIZE = HEX_RADIUS * 2 + 1

    GRID_CORNERS = [
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
            [None for i in range(Board.GRID_SIZE)]
            for j in range(Board.GRID_SIZE)
        ]

        tile_order = []
        for tile_cls in Tile.__subclasses__():
            tile_order += [tile_cls] * tile_cls.COUNT
        random.shuffle(tile_order)

        grid_order = []
        for grid_row in range(Board.GRID_SIZE):
            for grid_col in range(Board.GRID_SIZE):
                grid_diag = grid_col - grid_row
                if abs(grid_diag) <= Board.HEX_RADIUS: 
                    grid_order.append((grid_row, grid_col))
        random.shuffle(grid_order)

        for tile_cls, (grid_row, grid_col) in zip(tile_order, grid_order):
            hex_x, hex_y = Board.grid_to_hex(grid_row, grid_col)
            self.grid[grid_row][grid_col] = tile_cls(hex_x, hex_y)


        traversal = Board.spiral_traversal(Board.HEX_RADIUS)
        number_idx = 0
        for (grid_x, grid_y) in traversal:
            tile = self.grid[grid_x][grid_y]
            if isinstance(tile, DesertTile):
                tile.number = None
            else:
                tile.number = Board.DEFAULT_NUMBER_ORDER[number_idx]
                number_idx += 1

    @classmethod
    def grid_to_hex(cls, grid_row, grid_col):
        hex_x = grid_col - cls.HEX_RADIUS
        hex_y = cls.HEX_RADIUS - grid_row
        return (hex_x, hex_y)


    @classmethod
    def spiral_traversal(cls, hex_radius) -> List[Tile]:
        if hex_radius < 0:
            return []

        start_x, start_y = [cls.GRID_SIZE // 2 - hex_radius] * 2
        traversal = [(start_x, start_y)]

        for direction in cls.CCW_GRID_DIRECTIONS:
            dx, dy = direction
            for i in range(hex_radius):
                prev_x, prev_y = traversal[-1]
                traversal.append((prev_x + dx, prev_y + dy))

        if hex_radius > 0:
            del traversal[-1]

        return traversal + cls.spiral_traversal(hex_radius - 1)
