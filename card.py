import random

SUITS = ['h', 'c', 'd', 's']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __unicode__(self):
        return self.rank + self.suit

    def __str__(self):
        return self.rank + self.suit


class Hand():
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def __str__(self):
        return str(self.card1) + str(self.card2)


class Deck():
    def __init__(self):
        self.deck = [str(x) + str(y) for x in RANKS for y in SUITS]

    def deal(self):
        return self.deck.pop(random.randrange(0, len(self.deck)))


deck1 = Deck()
card1 = Card('A', 'h')
card2 = Card('K', 'h')
p1hand = Hand(card1, card2)

print deck1.deck

p1hand = Hand(deck1.deal(), deck1.deal())
print p1hand
print deck1.deck

p2hand = Hand(deck1.deal(), deck1.deal())
print p2hand
print deck1.deck
