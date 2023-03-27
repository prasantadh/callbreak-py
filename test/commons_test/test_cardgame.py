from commons.CardGame import CardGame

import unittest

class Testing(unittest.TestCase):

    def test_getters_and_setters(self):
        game = CardGame()
        assert(game.name == 'generic')

if __name__ == '__main__':
    unittest.main()