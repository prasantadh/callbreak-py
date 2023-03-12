import unittest

from commons.Suit import Suit

class Testing(unittest.TestCase):

    def test_suit_prints_correct_name_value(self):
        assert(str(Suit.Hukum) == '♠')
        assert(str(Suit.Chidi) == '♣')
        assert(str(Suit.Itta) == '♦')
        assert(str(Suit.Paan) == '♥')

if __name__ == '__main__':
    unittest.main()
