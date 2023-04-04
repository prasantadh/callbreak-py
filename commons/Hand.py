from commons.Card import Card
from commons.Suit import Suit 

class Hand:
    def __init__(self):
        self._cards = []
        pass

    def add(self, card):
        self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        self._cards = value
    
    def play(self, card):
        self._cards.remove(card)

    def sort(self):
        cards = []
        for suit in Suit:
            for card in self.cards:
                if card.suit == suit:
                    cards.append(card)
        self._cards = sorted(cards, reverse=True)

    def __repr__(self) -> str:
        return ','.join(str(card) for card in self.cards)
