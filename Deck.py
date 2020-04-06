from Card import Card
from random import shuffle, sample
from Hand import Hand

class Deck:
    suits = ['♠', '♥', '♣', '♦']
    ranks = ['A', 'J', 'Q', 'K'] + [str(i) for i in range(2, 11)]

    cards = []
    for suit in suits:
        for rank in ranks:
            cards.append(Card(suit, rank))

    def __init__(self):
        shuffle(self.cards)
        # TODO: Add rules to ensure shuffle valid per callbreak rules

    def shuffle(self):
        shuffle(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __str__(self):
        deck = ''
        for card in self.cards:
            deck = deck + '({}{}) '.format(card.suit, card.rank)
        return deck.strip()

    def deal(self, numberOfCards):
        return sample(self.cards, numberOfCards)

    def deal_hand(self, numberOfCards):
        currentHand = Hand()
        currentHand.addCards(sample(self.cards, numberOfCards))
        return currentHand

if __name__=='__main__':
    deck = Deck()
    print(deck)

    print(deck.deal(5))

    print(deck.deal_hand(13))