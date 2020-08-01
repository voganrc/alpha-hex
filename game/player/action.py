class Action:

    def __init__(self, fn, target):
        self.fn = fn
        self.target = target

    def apply(self):
        self.fn(self.target)


class EndTurn(Action):

    def __init__(self):
        self.fn = lambda *_: None
        self.target = None
