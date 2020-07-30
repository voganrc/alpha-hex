from itertools import islice

from game.board import Board
from game.phase import Phase
from game.player.base import Color, Player


class Game:
    POINTS_TO_WIN = 10

    def __init__(self, num_players=2):
        self.board = Board(self)
        self.players = [Player(self, color) for color in islice(Color, num_players)]
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
        self.active_player.take_turn()
        # if self.active_player.victory_points >= Game.POINTS_TO_WIN:
        if len(self.active_player.legal_moves()) == 0:
            self.phase = Phase.COMPLETED
        else:
            self.turn += 1
            if self.turn == 2 * len(self.players):
                self.phase = Phase.PLAY
