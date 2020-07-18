import random

from game.board import Board
from game.phase import Phase
from game.player.base import Player


class Game:

    def __init__(self):
        self.board = Board()
        self.phase = Phase.SET_UP

    def start(self):
        for player in Player:
            legal_vertices = self.board.legal_vertices(player, self.phase)
            random.choice(legal_vertices).settle(player)
        for player in Player:
            legal_vertices = self.board.legal_vertices(player, self.phase)
            random.choice(legal_vertices).settle(player)
