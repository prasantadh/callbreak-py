import unittest
from commons.Suit import Suit
from commons.Rank import Rank
from commons.Card import Card

class Testing(unittest.TestCase):

    def test_sanity(self):
        assert(True)

    def test_card_suit_and_rank(self):
        card = Card(suit=Suit.Hukum, rank=Rank.Ekka)
        assert(card.suit == Suit.Hukum)

if __name__ == '__main__':
    unittest.main()
