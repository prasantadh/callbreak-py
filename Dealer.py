from Deck import Deck
from CallBreak import Callbreak

class Dealer:
    def __init__(self, deck = Deck()):
        self.deck = deck
        self.hands = []

    def deal(self, game):
        self.deck.shuffle()
        for cardPosition in range(00, 13): self.hands[0].addCard(self.deck[])
        for cardPosition in range(13, 26): self.hands[1].addCard(self.deck[])
        for cardPosition in range(26, 39): self.hands[2].addCard(self.deck[])
        for cardPosition in range(39, 42): self.hands[3].addCard(self.deck[])
        return self.hands()

if __name__=='__main__':
    dealer = Dealer()

