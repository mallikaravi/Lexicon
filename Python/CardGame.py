from Deck import Deck
from Player import Player


class CardGame():
    def __init__(self) -> None:
        pass


def main():
    "Main method to run the Game"

    print("Welcome to War, let's begin...")

    deck = Deck()
    deck.shuffle()

    player = Player("Kumar")
    computer = Player("Computer")
    for i in range(10):
        player.draw(deck)
        computer.draw(deck)
    player.showHand()
    computer.showHand()

if __name__ == "__main__":
    main()
