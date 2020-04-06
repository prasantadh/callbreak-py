from Deck import Deck

class CardGame:
    def __init__(self, numberOfRounds=1, name='generic'):
        self.name = name
        self.players = []
        self.numberOfRounds=numberOfRounds

    def addPlayer(self, player):
        self.players.append(player)

    def __str__(self):
        return 'The {} game is on!'.format(self.name)

if __name__=='__main__':
    game = CardGame()
    print(game)
