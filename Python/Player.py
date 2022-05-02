
class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.hands = []

    def draw(self, deck):
        self.hands.append(deck.deal())
        return self

    def showHand(self):
        for hand in self.hands:
            hand.show()

    def discard(self):
        return self.hand.pop()