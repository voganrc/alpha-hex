# ============================================================================================================= #
#               Vertex Index                                        Grid Coordinates                            #
# ============================================================================================================= #
#                                                                                                               #
#                  5___6                                                                                        #
#                  /    \                                                                                       #
#            3___4/    14\__15                                                                                  #
#            /    \      /    \                                                                                 #
#      1___2/    12\__13/    25\__26            +----+----+----+----+----+----+----+----+----+----+----+----+   #
#      /    \      /    \      /    \           |  0 |  1 |  2 |  3 |  4 |  5 |  6 |    |    |    |    |    |   #
#    0/    10\__11/    23\__24/    37\          +----+----+----+----+----+----+----+----+----+----+----+----+   #
#     \      /    \      /    \      /          |  7 |  8 |  9 | 10 | 11 | 12 | 13 | 14 | 15 |    |    |    |   #
#     8\___9/    21\__22/    35\__36/           +----+----+----+----+----+----+----+----+----+----+----+----+   #
#      /    \      /    \      /    \           | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |    |   #
#    7/    19\__20/    33\__34/    46\   ===>   +----+----+----+----+----+----+----+----+----+----+----+----+   #
#     \      /    \      /    \      /          |    | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 |   #
#    17\__18/    31\__32/    44\__45/           +----+----+----+----+----+----+----+----+----+----+----+----+   #
#      /    \      /    \      /    \           |    |    |    | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 |   #
#   16/    29\__30/    42\__43/    53\          +----+----+----+----+----+----+----+----+----+----+----+----+   #
#     \      /    \      /    \      /          |    |    |    |    |    | 47 | 48 | 49 | 50 | 51 | 52 | 53 |   #
#    27\__28/    40\__41/    51\__52/           +----+----+----+----+----+----+----+----+----+----+----+----+   #
#           \      /    \      /                                                                                #
#          38\__39/    49\__50/                                                                                 #
#                 \      /                                                                                      #
#                47\__48/                                                                                       #
#                                                                                                               #
# ============================================================================================================= #
from game.indexing.base import Grid
from game.pieces.settlement import Settlement


class Vertex:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.building = None

    @property
    def points_up(self):
        return self.col % 2 == 1

    def settle(self, player):
        if self.building:
            raise ValueError("Vertex already settled")
        else:
            self.building = Settlement(self, player)


class VertexGrid(Grid):
    N_ROWS = 6
    N_COLS = 12
    INDICES = [
        [0, 1, 2, 3, 4, 5, 6, None, None, None, None, None],
        [7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None],
        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, None],
        [None, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
        [None, None, None, 38, 39, 40, 41, 42, 43, 44, 45, 46],
        [None, None, None, None, None, 47, 48, 49, 50, 51, 52, 53],
    ]

    def __init__(self):
        self.elements = []
        for row in range(VertexGrid.N_ROWS):
            for col in range(VertexGrid.N_COLS):
                if VertexGrid.INDICES[row][col] is not None:
                    self.elements.append(Vertex(row, col))

    def vertices_for_hex(self, hex_):
        vertex_row_above = hex_.row
        vertex_col_left = 2 * hex_.col
        vertices = []
        for d_row in range(2):
            for d_col in range(3):
                vertex_row = vertex_row_above + d_row
                vertex_col = vertex_col_left + d_row + d_col
                vertices.append(self.get(vertex_row, vertex_col))
        return [vertex for vertex in vertices if vertex]

    def vertices_for_edge(self, edge):
        vertex_row_first = edge.row // 2
        vertex_row_second = edge.row // 2 + 1 if edge.is_vertical else edge.row // 2
        vertex_col_first = edge.col
        vertex_col_second = edge.col + 1
        return [
            self.get(vertex_row_first, vertex_col_first),
            self.get(vertex_row_second, vertex_col_second),
        ]

    @staticmethod
    def sort(vertices):
        return sorted(vertices, key=lambda vertex: VertexGrid.INDICES[vertex.row][vertex.col])
