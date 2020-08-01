from itertools import islice

from game.board import Board
from game.phase import Phase
from game.player.action import EndTurn
from game.player.base import Color, Player


class Game:
    POINTS_TO_WIN = 10

    def __init__(self, num_players=2):
        self.board = Board(self)
        self.players = [Player(self, color) for color in islice(Color, num_players)]
        self.last_action = None
        self.phase = Phase.SET_UP
        self.turn = 0

    @property
    def active_player(self):
        if self.turn < len(self.players):
            return self.players[self.turn]
        elif self.turn < 2 * len(self.players):
            return self.players[2 * len(self.players) - self.turn - 1]
        else:
            return self.players[self.turn % len(self.players)]

    @property
    def winner(self):
        return self.active_player if self.phase == Phase.COMPLETED else None

    def advance(self):
        if self.phase == Phase.COMPLETED:
            return
        self.active_player.take_action()
        self.maybe_update_phase()
        self.maybe_update_turn()

    def maybe_update_phase(self):
        if isinstance(self.last_action, EndTurn) and self.turn == 2 * len(self.players) - 1:
            self.phase = Phase.PLAY
        elif len(self.active_player.legal_actions()) == 0:
            self.phase = Phase.COMPLETED

    def maybe_update_turn(self):
        if isinstance(self.last_action, EndTurn):
            self.turn += 1
