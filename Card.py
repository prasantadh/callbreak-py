class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.faceRanks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}

    def __str__(self):
        return self.suit + self.rank

    def getRankValue(self):
    	if self.rank in self.faceRanks.keys():
    		return self.faceRanks[self.rank]
    	else:
    		return int(self.rank)

    def __lt__(self, otherCard):
    	return self.getRankValue() < otherCard.getRankValue()

    def __eq__(self, otherCard):
    	if isinstance(otherCard, Card):
    		return self.getRankValue() == otherCard.getRankValue()
    	return False

if __name__=='__main__':
    card = Card('Hukum-ko-','Ekka')
    print(card)

    print(Card('♠','A') == Card('♠','A'))
    print(Card('♠','J') < Card('♦','A'))
    print(Card('♣','5') < Card('♠','2'))