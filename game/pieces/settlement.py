class Settlement:

    def __init__(self, player, vertex):
        self.player = player
        self.vertex = vertex

    def pay(self, resource):
        if resource:
            self.player.hand.draw_cards(1, resource)
