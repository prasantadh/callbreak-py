class Haat:

    def __init__(self, players):
        self.players=players
        self.haatHistory=[(0,""),(0,""),(0,""),(0,"")]

    def runHaat(self):
        for i in range(0,4):
            num, suit=players[i].playTurn(self.haatHistory,i)
            self.playHistory[i]=(num,suit)

    def findWinningHaat(self):
        pass
