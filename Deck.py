from Card import Card
from random import shuffle, sample
from Hand import Hand
from Suit import Suit
from Rank import Rank

class Deck:

    def __init__(self):
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)

    def __str__(self):
        self.sort()
        deck = ''
        for card in self.cards:
            deck = deck + '({} {}) '.format(card.suit, card.rank)
        return deck.strip()

    def deal(self):
        return self.cards.pop()

    def sort(self):
        """
        Sort the current deck such that all ranks are in descending order
        and the suits are in the order ♠, ♥, ♣, ♦.
        """
        self.cards = sorted(self.cards, key=lambda card: (card.suit, card.rank), reverse=True)

if __name__=='__main__':
    deck = Deck()
    print(deck)
