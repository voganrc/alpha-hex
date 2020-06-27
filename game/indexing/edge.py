# ======================================================================================================== #
#               Edge Index                                           Grid Coordinates                      #
# ======================================================================================================== #
#                                                                                                          #
#                                               +----+----+----+----+----+----+----+----+----+----+----+   #
#                  __5_                         |  0 |  1 |  2 |  3 |  4 |  5 |    |    |    |    |    |   #
#                4/    \9                       +----+----+----+----+----+----+----+----+----+----+----+   #
#            __3_/      \_17_                   |  6 |    |  7 |    |  8 |    |  9 |    |    |    |    |   #
#          2/    \8   16/    \22                +----+----+----+----+----+----+----+----+----+----+----+   #
#      __1_/      \_15_/      \_32_             | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |    |    |    |   #
#    0/    \7   14/    \21  31/    \38          +----+----+----+----+----+----+----+----+----+----+----+   #
#    /      \_13_/      \_30_/      \           | 18 |    | 19 |    | 20 |    | 21 |    | 22 |    |    |   #
#    \6   12/    \20  29/    \37  48/           +----+----+----+----+----+----+----+----+----+----+----+   #
#     \_11_/      \_28_/      \_47_/            | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |    |   #
#   10/    \19  27/    \36  46/    \53          +----+----+----+----+----+----+----+----+----+----+----+   #
#    /      \_26_/      \_45_/      \    ===>   | 33 |    | 34 |    | 35 |    | 36 |    | 37 |    | 38 |   #
#    \18  25/    \35  44/    \52  61/           +----+----+----+----+----+----+----+----+----+----+----+   #
#     \_24_/      \_43_/      \_60_/            |    | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 |   #
#   23/    \34  42/    \51  59/    \65          +----+----+----+----+----+----+----+----+----+----+----+   #
#    /      \_41_/      \_58_/      \           |    |    | 49 |    | 50 |    | 51 |    | 52 |    | 53 |   #
#    \33  40/    \50  57/    \64  71/           +----+----+----+----+----+----+----+----+----+----+----+   #
#     \_39_/      \_56_/      \_70_/            |    |    |    | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 |   #
#          \49  55/    \63  69/                 +----+----+----+----+----+----+----+----+----+----+----+   #
#           \_54_/      \_68_/                  |    |    |    |    | 62 |    | 63 |    | 64 |    | 65 |   #
#                \62  67/                       +----+----+----+----+----+----+----+----+----+----+----+   #
#                 \_66_/                        |    |    |    |    |    | 66 | 67 | 68 | 69 | 70 | 71 |   #
#                                               +----+----+----+----+----+----+----+----+----+----+----+   #
#                                                                                                          #
# ======================================================================================================== #
from game.indexing.base import Grid


class Edge:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def points_up(self):
        return self.row % 2 == 1 and self.col % 2 == 0


class EdgeGrid(Grid):
    N_ROWS = 11
    N_COLS = 11
    INDICES = [
        [0, 1, 2, 3, 4, 5, None, None, None, None, None],
        [6, None, 7, None, 8, None, 9, None, None, None, None],
        [10, 11, 12, 13, 14, 15, 16, 17, None, None, None],
        [18, None, 19, None, 20, None, 21, None, 22, None, None],
        [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, None],
        [33, None, 34, None, 35, None, 36, None, 37, None, 38],
        [None, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
        [None, None, 49, None, 50, None, 51, None, 52, None, 53],
        [None, None, None, 54, 55, 56, 57, 58, 59, 60, 61],
        [None, None, None, None, 62, None, 63, None, 64, None, 65],
        [None, None, None, None, None, 66, 67, 68, 69, 70, 71],
    ]

    def __init__(self):
        self.elements = []
        for row in range(EdgeGrid.N_ROWS):
            for col in range(EdgeGrid.N_COLS):
                if EdgeGrid.INDICES[row][col] is not None:
                    self.elements.append(Edge(row, col))

    def edges_for_vertex(self, vertex):
        edge_row_center = vertex.row * 2
        edge_col_right = vertex.col
        edges = []
        if vertex.points_up:
            edges.append(self.get(edge_row_center - 1, edge_col_right - 1))
            edges.append(self.get(edge_row_center, edge_col_right - 1))
            edges.append(self.get(edge_row_center, edge_col_right))
        else:
            edges.append(self.get(edge_row_center, edge_col_right - 1))
            edges.append(self.get(edge_row_center, edge_col_right))
            edges.append(self.get(edge_row_center + 1, edge_col_right))
        return [edge for edge in edges if edge]
