import unittest
from commons.Rank import Rank

class Testing(unittest.TestCase):

    def test_rank_return_correct_str_repr(self):
        for rank in Rank:
            if rank.value < 11:
                assert(str(rank.value) == str(rank))
            else:
                assert(str(rank) == ['J', 'Q', 'K', 'A'][rank.value - 11])

if __name__ == '__main__':
    unittest.main()
