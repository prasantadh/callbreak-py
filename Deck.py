from Card import Card
from random import shuffle

class Deck:
    suits = ['♠', '♥', '♣', '♦']
    ranks = ['A', 'J', 'Q', 'K'] + [str(i) for i in range(2, 11)]

    cards = []
    for suit in suits:
        for rank in ranks:
            cards.append(Card(suit, rank))

    def __init__(self):
        shuffle(self.cards)

    def __str__(self):
        deck = ''
        for card in self.cards:
            deck = deck + '({}{}) '.format(card.suit, card.rank)
        return deck.strip()

if __name__=='__main__':
    deck = Deck()
    print(deck)


