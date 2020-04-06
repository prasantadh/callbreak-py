class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

if __name__=='__main__':
    card = Card('Hukum-ko-','Ekka')
    print(card)
