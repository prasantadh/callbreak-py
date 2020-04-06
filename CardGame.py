from Deck import Deck

class CardGame:
    def __init__(self):
        players = []

    def addPlayer(self, player):
        players.append(player)

    def __str__(self):
        return 'The game is on!'

if __name__=='__main__':
    game = CardGame()
    print(game)


