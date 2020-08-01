from enum import Enum

from game.pieces.road import Road
from game.pieces.settlement import Settlement
from game.player.actor import Actor
from game.player.hand import Hand


class Color(Enum):
    RED = 0
    BLUE = 1
    WHITE = 2
    ORANGE = 3


class Player(Actor):

    def __init__(self, game, color):
        self.game = game
        self.color = color

        self.hand = Hand()
        self.roads = []
        self.settlements = []

    @property
    def victory_points(self):
        return len(self.settlements)

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

    def take_action(self):
        action = self.choose_action()
        if action:
            action.apply()
        self.game.last_action = action
