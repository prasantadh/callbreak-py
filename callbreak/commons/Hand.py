from . import Card

class Hand:
    def __init__(self):
        self.cards = []

    def addCards(self, cards):
    	self.cards = cards

    def playHand(self, card):
    	'''
    		This should remove the currently played hand from the Hand cards list.
    	'''
    	pass


    def __str__(self):
        self.sort()
        return ''.join(str(card)+' ' for card in self.cards).strip()

    def addCard(self, card):
        self.cards.append(card)

    def sort(self):
        pass

if __name__ == '__main__':
    hand = Hand()
    print(hand)
