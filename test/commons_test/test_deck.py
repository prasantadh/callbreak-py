import unittest
from commons.Rank import Rank
from commons.Suit import Suit
from commons.Deck import Deck
from commons.Card import Card

class Testing(unittest.TestCase):

    def test_sanity(self):
        deck = str(Deck())
        for suit in Suit:
            for rank in Rank:
                assert(str(suit) + str(rank) in deck)

if __name__ == '__main__':
    unittest.main()
