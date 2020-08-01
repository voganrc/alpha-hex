import random
from enum import Enum

from game.phase import Phase
from game.pieces.road import Road
from game.pieces.settlement import Settlement
from game.player.action import Action, EndTurn


class Color(Enum):
    RED = 0
    BLUE = 1
    WHITE = 2
    ORANGE = 3


class Player:

    def __init__(self, game, color):
        self.game = game
        self.color = color

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

    def choose_action(self):
        PHASE_TO_ACTION_CHOOSER = {
            Phase.SET_UP: self._choose_set_up_action,
            Phase.PLAY: self._choose_play_action,
            Phase.COMPLETED: lambda *_: None,
        }
        return PHASE_TO_ACTION_CHOOSER[self.game.phase]()

    def legal_actions(self):
        settle_actions = [Action(self.settle, vertex) for vertex in self.game.board.legal_vertices(self)]
        pave_actions = [Action(self.pave, edge) for edge in self.game.board.legal_edges(self)]
        return settle_actions + pave_actions

    def _choose_set_up_action(self):
        if self._starting_placement_complete():
            return EndTurn()
        else:
            return self._starting_placement()

    def _starting_placement_complete(self):
        if self.game.phase != Phase.SET_UP:
            return True
        return self.game.last_action and self.game.last_action.fn == self.pave

    def _starting_placement(self):
        if len(self.settlements) == len(self.roads):
            return self._place_starting_settlement()
        else:
            return self._place_starting_road()

    def _place_starting_settlement(self):
        legal_vertices = self.game.board.legal_vertices(self)
        return Action(self.settle, random.choice(legal_vertices))

    def _place_starting_road(self):
        last_settled_vertex = self.settlements[-1].vertex
        legal_edges = self.game.board.edge_grid.edges_for_vertex(last_settled_vertex)
        return Action(self.pave, random.choice(legal_edges))

    def _choose_play_action(self):
        if not isinstance(self.game.last_action, EndTurn):
            return EndTurn()
        legal_actions = self.legal_actions()
        return random.choice(legal_actions) if legal_actions else None
