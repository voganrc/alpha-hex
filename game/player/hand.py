from collections import Counter

from game.pieces.resource import Resource


class Hand:

    def __init__(self):
        self.card_counts = Counter()

    def __str__(self):
        d = {resource.name: self.card_counts[resource] for resource in Resource}
        s = ""
        for k in d:
            s += f"{k}: {d[k]}\n"
        return s

    def draw_cards(self, amount, card):
        self.card_counts[card] += amount
