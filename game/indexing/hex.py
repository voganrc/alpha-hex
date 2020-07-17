# ======================================================================== #
#               Hex Index                          Grid Coordinates        #
# ======================================================================== #
#                                                                          #
#                 ____                                                     #
#                /    \                                                    #
#           ____/   2  \____                                               #
#          /    \      /    \                                              #
#     ____/   1  \____/   6  \____                                         #
#    /    \      /    \      /    \           +----+----+----+----+----+   #
#   /   0  \____/   5  \____/  11  \          |  0 |  1 |  2 |    |    |   #
#   \      /    \      /    \      /          +----+----+----+----+----+   #
#    \____/   4  \____/  10  \____/           |  3 |  4 |  5 |  6 |    |   #
#    /    \      /    \      /    \           +----+----+----+----+----+   #
#   /   3  \____/   9  \____/  15  \   ===>   |  7 |  8 |  9 | 10 | 11 |   #
#   \      /    \      /    \      /          +----+----+----+----+----+   #
#    \____/   8  \____/  14  \____/           |    | 12 | 13 | 14 | 15 |   #
#    /    \      /    \      /    \           +----+----+----+----+----+   #
#   /   7  \____/  13  \____/  18  \          |    |    | 16 | 17 | 18 |   #
#   \      /    \      /    \      /          +----+----+----+----+----+   #
#    \____/  12  \____/  17  \____/                                        #
#         \      /    \      /                                             #
#          \____/  16  \____/                                              #
#               \      /                                                   #
#                \____/                                                    #
#                                                                          #
# ======================================================================== #
from typing import List

from game.indexing.base import Grid


class Hex:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.tile = None


class HexGrid(Grid):
    N_ROWS = 5
    N_COLS = 5
    INDICES = [
        [0, 1, 2, None, None],
        [3, 4, 5, 6, None],
        [7, 8, 9, 10, 11],
        [None, 12, 13, 14, 15],
        [None, None, 16, 17, 18],
    ]

    def __init__(self):
        self.elements = []
        for row in range(HexGrid.N_ROWS):
            for col in range(HexGrid.N_COLS):
                if HexGrid.INDICES[row][col] is not None:
                    self.elements.append(Hex(row, col))

    def hexes_for_vertex(self, vertex):
        hex_row_above = vertex.row - 1
        hex_row_below = vertex.row
        hex_col_left = vertex.col // 2 - 1
        hex_col_right = vertex.col // 2
        hexes = []
        if vertex.points_up:
            hexes.append(self.get(hex_row_above, hex_col_left))
            hexes.append(self.get(hex_row_above, hex_col_right))
            hexes.append(self.get(hex_row_below, hex_col_right))
        else:
            hexes.append(self.get(hex_row_above, hex_col_left))
            hexes.append(self.get(hex_row_below, hex_col_left))
            hexes.append(self.get(hex_row_below, hex_col_right))
        return [hex_ for hex_ in hexes if hex_]

    def spiral_traversal(self, layer=None) -> List[Hex]:
        """counter-clockwise"""

        SPIRAL_STEPS = [
            (+1, +0),  # step down
            (+1, +1),  # step down-right
            (+0, +1),  # step right
            (-1, +0),  # step up
            (-1, -1),  # step up-left
            (+0, -1),  # step left
        ]

        if layer is None:
            layer = HexGrid.N_ROWS // 2
        elif layer < 0:
            return []

        start_coords = tuple([HexGrid.N_ROWS // 2 - layer]) * 2
        traversal = [self.get(*start_coords)]

        for d_row, d_col in SPIRAL_STEPS:
            for i in range(layer):
                prev_row, prev_col = traversal[-1].row, traversal[-1].col
                traversal.append(self.get(prev_row + d_row, prev_col + d_col))

        if layer > 0:
            traversal.pop(-1)

        return traversal + self.spiral_traversal(layer - 1)
