from random import randint


class Dice:

    def __init__(self):
        self.rolled = False
        self.first_die = 1
        self.second_die = 1

    @property
    def sum(self) -> int:
        return self.first_die + self.second_die

    def roll(self) -> 'Dice':
        self.first_die = randint(1, 6)
        self.second_die = randint(1, 6)
        self.rolled = True
        return self

    def update_turn(self) -> None:
        self.rolled = False
