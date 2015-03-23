import unittest
from pokertools.hand import Hand

class TestHandEvals(unittest.TestCase):
    def test_pair(self):
        hand = Hand('Ah', 'Ac', 'Kd', 'Qs', '2h')
        self.assertEqual('pair', hand.eval())

    def test_trips(self):
        hand = Hand('Ah', 'Ad', 'Ac', '2s', '3h')
        self.assertEqual('trips', hand.eval())

    def test_two_pair(self):
        hand = Hand('Ah', 'Ad', 'Kh', 'Kd', '2c')
        self.assertEqual('two-pair', hand.eval())

    def test_straight(self):
        hand = Hand('Ah', 'Kc', 'Qd', 'Js', 'Tc')
        self.assertEqual('straight', hand.eval())

    def test_flush(self):
        hand = Hand('2h', '4h', '5h', 'Th', 'Ah')
        self.assertEqual('flush', hand.eval())

    def test_full_house(self):
        hand = Hand('Ah', 'Ad', 'Ac', 'Kh', 'Ks')
        self.assertEqual('full-house', hand.eval())

    def test_high_card(self):
        hand = Hand('Ah', 'Js', 'Tc', '7d', '2h')
        self.assertEqual('high-card A', hand.eval())

    def test_straight_flush(self):
        hand = Hand('Th', '9h', '8h', '7h', '6h')
        self.assertEqual('straight-flush', hand.eval())

    def test_quads(self):
        hand = Hand('Ah', 'Ac', 'As', 'Ad', '2h')
        self.assertEqual('quads', hand.eval())

    def test_royal_flush(self):
        hand = Hand('Ah', 'Kh', 'Qh', 'Jh', 'Th')
        self.assertEqual('royal-flush', hand.eval())
