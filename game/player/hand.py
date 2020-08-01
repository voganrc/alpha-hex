from collections import Counter


class Hand:

    def __init__(self):
        self.card_counts = Counter()

    def draw_cards(self, amount, card):
        self.card_counts[card] += amount
