import unittest

from commons.Suit import Suit

class Testing(unittest.TestCase):

    def test_suit_prints_correct_name_value(self):
        assert(str(Suit.Hukum) == '♠')
        assert(str(Suit.Chidi) == '♣')
        assert(str(Suit.Itta) == '♦')
        assert(str(Suit.Paan) == '♥')

    def test_suit_comparison(self):
        assert(Suit.Hukum == Suit.Hukum)
        assert(Suit.Chidi == Suit.Chidi)
        assert(Suit.Itta == Suit.Itta)
        assert(Suit.Paan == Suit.Paan)
        assert(Suit.Hukum > Suit.Chidi)
        assert(Suit.Hukum > Suit.Itta)
        assert(Suit.Hukum > Suit.Paan)
        assert(Suit.Chidi > Suit.Itta)
        assert(Suit.Itta > Suit.Chidi)

if __name__ == '__main__':
    unittest.main()
