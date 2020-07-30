import random
from enum import Enum

from game.phase import Phase
from game.pieces.road import Road
from game.pieces.settlement import Settlement


class Color(Enum):
    RED = 0
    BLUE = 1
    WHITE = 2
    ORANGE = 3


class Move:

    def __init__(self, fn, target):
        self.fn = fn
        self.target = target

    def apply(self):
        return self.fn(self.target)


class Player:

    def __init__(self, game, color):
        self.game = game
        self.color = color

        self.roads = []
        self.settlements = []

    @property
    def victory_points(self):
        return len(self.settlements)

    def take_turn(self):
        if self.game.phase == Phase.SET_UP:
            self.place_starting_settlement()
        elif self.game.phase == Phase.PLAY:
            legal_moves = self.legal_moves()
            if legal_moves:
                random.choice(legal_moves).apply()
        elif self.game.phase == Phase.COMPLETED:
            return
        else:
            raise ValueError("Invalid game phase")

    def place_starting_settlement(self):
        settled_vertex = self.settle(
            random.choice(self.game.board.legal_vertices(self))
        )
        paved_edge = self.pave(
            random.choice(self.game.board.edge_grid.edges_for_vertex(settled_vertex))
        )
        return settled_vertex, paved_edge

    def legal_moves(self):
        settle_moves = [Move(self.settle, vertex) for vertex in self.game.board.legal_vertices(self)]
        pave_moves = [Move(self.pave, edge) for edge in self.game.board.legal_edges(self)]
        return settle_moves + pave_moves

    def settle(self, vertex):
        if vertex.building:
            raise ValueError("Vertex already settled")
        new_settlement = Settlement(self, vertex)
        vertex.building = new_settlement
        self.settlements.append(new_settlement)
        return vertex

    def pave(self, edge):
        if edge.road:
            raise ValueError("Edge already paved")
        new_road = Road(self, edge)
        edge.road = new_road
        self.roads.append(new_road)
        return edge
