from CardGame import CardGame
# from Renderer import Renderer


class CallBreak(CardGame):
    numberOfPlayers = 4

    def __init__(self):
        super().__init__(name='CallBreak')
        self.totalRound = 5
        self.currentRound = 0

    def play(self):
        for player in self.players:
            for i in range(13):
                player.addCard(self.deck.deal())
            # print(player)

if __name__ == '__main__':
    game = CallBreak()
    print(game)
