import random

from Hand import Hand
# Two useful variables for creating Cards.
# TODO Shall be reated constants file for SUITS, RANKS etc
SUITS = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        "Preparing the cards array"
        "Iterate through RANKS and SUIT and append it to cards array"
        for value in RANKS:
            for suit in SUITS:
                self.cards.append(Hand(suit, value))

    def shuffle(self):
        "Using random library and shuffling the cards"
        random.shuffle(self.cards)

    def deal(self):
        "Deal the card from the deck using the pop method"
        if len(self.cards) > 1:
            return self.cards.pop()
