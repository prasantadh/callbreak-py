from Round import Round

class CallBreakRound(Round):

    def __init__():
        super.__init__(roundNum, 4, seating, startDealer, 13)
        self._playersBid=[0,0,0,0]
        self._playersHandsWon=[0,0,0,0]
        self._playerScore=[0,0,0,0]

    def runRound(self):
        for i in range(0, self.totalPlays):
            # initialize play, set it to self.currentPlay
            # run Play
            # get winner
            self.currentPlayNum+=1
        pass
        #returns self.getFinalScore

    def getFinalScore(self):
        return self._playersScore
