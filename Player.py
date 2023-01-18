from Hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.score = 0
        self.cards = []

    def __str__(self):
        return self.name

    def addCard(self, card):
        self.cards.append(card)

    def setHand(self, hand):
        self.hand = hand

    def getHand(self):
        return self.hand




# play hand
# number of winning hands
#

if __name__ == '__main__':
    player = Player('Player 1')
    print(player)
