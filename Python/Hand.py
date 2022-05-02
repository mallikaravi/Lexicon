
class Hand():
    def __init__(self, suit, val) -> None:
        self.suit = suit
        self.value = val

    def add(self, card):
        ""

    def remove(self):
        ""

    def show(self):
        "Print out the card, so we make a string that will print \
        out the value and the suit"
        print("{} of {}".format(self.value, self.suit))
