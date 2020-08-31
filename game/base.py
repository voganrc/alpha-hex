from itertools import islice

from game.board import Board
from game.phase import Phase
from game.pieces.dice import Dice
from game.player.action import EndTurnAction
from game.player.base import Color, Player


class Game:
    POINTS_TO_WIN = 6

    def __init__(self, num_players=2):
        self.board = Board(self)
        self.players = [Player(self, color) for color in islice(Color, num_players)]
        self.phase = Phase.SET_UP
        self.dice = Dice()
        self.last_action = None
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
        elif self.phase == Phase.PLAY and not self.dice.rolled:
            self.board.handle_roll(self.dice.roll())
            return
        self.active_player.take_action()
        self.maybe_update_phase()
        self.maybe_update_turn()

    def maybe_update_phase(self):
        if self.turn == 2 * len(self.players) - 1 and isinstance(self.last_action, EndTurnAction):
            self.phase = Phase.PLAY
        elif self.active_player.victory_points >= Game.POINTS_TO_WIN:
            self.phase = Phase.COMPLETED

    def maybe_update_turn(self):
        if isinstance(self.last_action, EndTurnAction):
            self.turn += 1
            self.dice.update_turn()
