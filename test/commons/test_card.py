import unittest
from commons.Suit import Suit
from commons.Rank import Rank
from commons.Card import Card

class Testing(unittest.TestCase):

    def test_card_sanity(self):
        card = Card(suit=Suit.Hukum, rank=Rank.Ekka)
        assert(str(card) == str(card.suit) + str(card.rank) )

if __name__ == '__main__':
    unittest.main()
