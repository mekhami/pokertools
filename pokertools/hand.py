class Hand():
    def __init__(self, *cards):
        self.cards = [x for x in cards]

    def __str__(self):
        return str(self.cards)

    def eval(self):
        if len(set([x[1] for x in self.cards])) == 1 and ('AKQJT' in [x[0] for x in self.cards]):
            return 'royal flush'
        if len(set([x[1] for x in self.cards])) == 1:
            return 'flush'
        if len(set([x[0] for x in self.cards])) == 4: 
            return 'pair'
