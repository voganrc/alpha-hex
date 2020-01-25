from tile import Tile
import random


#  Physical         Grid
#   Board          Mapping
# -------------------------
#   a b c         a b c . .
#  d e f g        d e f g .
# h i j k l  -->  h i j k l
#  m n o p        . m n o p
#   q r s         . . q r s
   

class Board:

    HEX_RADIUS = 2
    GRID_SIZE = HEX_RADIUS * 2 + 1

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

    @classmethod
    def grid_to_hex(cls, grid_row, grid_col):
        hex_x = grid_col - cls.HEX_RADIUS
        hex_y = cls.HEX_RADIUS - grid_row
        return (hex_x, hex_y)
