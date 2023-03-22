import unittest
from commons.Suit import Suit
from commons.Rank import Rank
from commons.Card import Card

class Testing(unittest.TestCase):

    def test_card_sanity(self):
        card = Card(suit=Suit.Hukum, rank=Rank.Ekka)
        assert(str(card) == '{} {}'.format(str(card.suit), str(card.rank)) )

    def test_card_comparison(self):
        assert(Card(Suit.Hukum, Rank.Dua) == Card(Suit.Hukum, Rank.Dua))
        assert(not Card(Suit.Hukum, Rank.Dua) == Card(Suit.Paan, Rank.Ekka))
        assert(Card(Suit.Hukum, Rank.Dua) > Card(Suit.Paan, Rank.Ekka))
        assert(Card(Suit.Hukum, Rank.Dua) > Card(Suit.Paan, Rank.Ekka))
        assert(Card(Suit.Hukum, Rank.Dua) < Card(Suit.Hukum, Rank.Tirka))
        assert(Card(Suit.Paan, Rank.Dua) > Card(Suit.Chidi, Rank.Ekka))

if __name__ == '__main__':
    unittest.main()
