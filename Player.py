from Hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        return self.name

    def setHand(self, hand):
        self.hand = hand

    def getHand(self):
        return self.hand


if __name__ == '__main__':
    player = Player('Player 1')
    print(player)
