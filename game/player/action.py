from abc import ABC, abstractmethod
from collections import Counter
from enum import Enum

from game.pieces.resource import Resource


class ActionType(Enum):
    SETTLE = 0
    PAVE = 1
    END_TURN = 2


class Action(ABC):
    COST = None

    @abstractmethod
    def __init__(self, player, target, is_free):
        self.player = player
        self.target = target
        self.is_free = is_free
        self.fn = None

    def is_affordable(self):
        return self.is_free or not (self.COST - self.player.hand.card_counts)

    def apply(self):
        self.fn(self.target)


class SettleAction(Action):
    COST = Counter({
        Resource.BRICK: 1,
        Resource.LUMBER: 1,
        Resource.GRAIN: 1,
        Resource.WOOL: 1,
    })

    def __init__(self, player, target, is_free=True):
        super().__init__(player, target, is_free)
        self.fn = self.player.settle


class PaveAction(Action):
    COST = Counter({
        Resource.BRICK: 1,
        Resource.LUMBER: 1,
    })

    def __init__(self, player, target, is_free=True):
        super().__init__(player, target, is_free)
        self.fn = self.player.pave


class EndTurnAction(Action):
    def __init__(self, player):
        super().__init__(player, None, True)
        self.fn = lambda *_: None
