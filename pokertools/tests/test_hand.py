import unittest
from pokertools.hand import Hand

class TestHandEvals(unittest.TestCase):
    def test_pair(self):
        hand = Hand('Ah', 'Ac', 'Kd', 'Qs', '2h')
        self.assertEqual('pair', hand.eval())

