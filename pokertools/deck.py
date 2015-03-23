import random

SUITS = ['h', 'c', 'd', 's']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']


class Deck():
    def __init__(self):
        self.deck = [str(x) + str(y) for x in RANKS for y in SUITS]

    def deal(self):
        return self.deck.pop(random.randrange(0, len(self.deck)))


deck = Deck()
hand1 = Hand(deck.deal(), deck.deal(), deck.deal(), deck.deal(), deck.deal())
print hand1
print hand1.eval()

hand2 = Hand('Ah', 'Kh', 'Qh', 'Jh', 'Th')
print hand2.eval()
