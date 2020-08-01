import random

from game.phase import Phase
from game.player.action import SettleAction, PaveAction, EndTurnAction


class _SetUpActor:

    def __init__(self):
        raise NotImplementedError

    def choose_set_up_action(self):
        if self._finished_starting_placement():
            return EndTurnAction(self)
        elif len(self.settlements) == len(self.roads):
            return self._starting_settle_action()
        else:
            return self._starting_pave_action()

    def _finished_starting_placement(self):
        assert self.game.phase == Phase.SET_UP
        return isinstance(self.game.last_action, PaveAction)

    def _starting_settle_action(self):
        legal_vertices = self.game.board.legal_vertices(self)
        return SettleAction(self, random.choice(legal_vertices), is_free=True)

    def _starting_pave_action(self):
        last_settled_vertex = self.settlements[-1].vertex
        legal_edges = self.game.board.edge_grid.edges_for_vertex(last_settled_vertex)
        return PaveAction(self, random.choice(legal_edges), is_free=True)


class _PlayActor:

    def __init__(self):
        raise NotImplementedError

    def choose_play_action(self):
        if not isinstance(self.game.last_action, EndTurnAction):
            return EndTurnAction(self)
        legal_actions = self._legal_play_actions()
        return random.choice(legal_actions) if legal_actions else None

    def _legal_play_actions(self):
        settle_actions = [SettleAction(self, vertex) for vertex in self.game.board.legal_vertices(self)]
        pave_actions = [PaveAction(self, edge) for edge in self.game.board.legal_edges(self)]
        return list(filter(
            lambda action: action.is_affordable(),
            settle_actions + pave_actions
        ))


class Actor(_SetUpActor, _PlayActor):

    def __init__(self):
        raise NotImplementedError

    def choose_action(self):
        PHASE_TO_ACTION_CHOOSER = {
            Phase.SET_UP: self.choose_set_up_action,
            Phase.PLAY: self.choose_play_action,
        }
        return PHASE_TO_ACTION_CHOOSER[self.game.phase]()
