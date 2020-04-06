from Card import Card
from random import shuffle, sample
from Hand import Hand
from utilities import sorting_card_keyy

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
        self.sort()
        deck = ''
        for card in self.cards:
            deck = deck + '({} {}) '.format(card.suit, card.rank)
        return deck.strip()

    def deal(self, numberOfCards):
        return sample(self.cards, numberOfCards)

    def deal_hand(self, numberOfCards):
        currentHand = Hand()
        currentHand.addCards(sample(self.cards, numberOfCards))
        return currentHand

    def sort(self):
        """
        Sort the current deck such that all ranks are in descending order
        and the suits are in the order ♠, ♥, ♣, ♦.
        """
        self.cards = sorted(self.cards, key=sorting_card_keyy, reverse=True)

if __name__=='__main__':
    deck = Deck()

    print(deck)

    a = deck.deal_hand(13)
    
    print(a)

    a.sort()

    print(a)


    a.sort()

    print(a)