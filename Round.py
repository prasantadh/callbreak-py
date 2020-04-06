class Round:

    def __init__(self, roundNum, numPlayers, seating, startDealer, totalPlays):
        self.numPlayers=numPlayers
        self.playersSeating=seating
        self.dealer=self.findDealer(startDealer, roundNum, playersSeating)
        self.totalPlays=totalPlays
        self.currentPlayNum=0
        self.currrentPlay=None



    def findDealer(self, startingDealer, roundNum, playersSeating):
        pass

    def runRound(self):
        pass
