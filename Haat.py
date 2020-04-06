class Haat:

    def __init__(self, players):
        self.players=players
        self.haatHistory=[(0,""),(0,""),(0,""),(0,"")]

    def runHaat(self):
        num, suit=players[i].playTurn(self.haatHistory,i)
        self.haatHistory[i]=(num,suit)
        for i in range(0,4):
            rank, suit=players[i].playTurn(self.haatHistory,i)
            self.haatHistory[i]=(rank,suit)
        return self.findWinningHaat()

    def findWinningHaat(self):
        winningPlayerInd=0
        stSuit=haatHistory[0][1]
        winningHaat=haatHistory[0]
        for i in range(1,4):
            if playHistory[i][1]=='♠' and winningHaat[1]!='♠':
                winningHaat=haatHistory[i]
                winningPlayerInd=i
            elif playHistory[i][1]=='♠' and winningHaat[1]=='♠':
                if winningHaat[i][0] < playHistory[i][0]:
                    winningHaat=haatHistory[i]
                    winningPlayerInd=i
            elif playHistory[i][1]==stSuit and winningHaat[1]=stSuit:
                if winningHaat[0] < playHistory[i][0]:
                    winningHaat=haatHistory[i]
                    winningPlayerInd=i
        return winningPlayerInd
