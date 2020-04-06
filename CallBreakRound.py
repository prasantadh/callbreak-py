from Round import Round

class CallBreakRound(Round):

    def __init__():
        super.__init__(roundNum, 4, seating, startDealer, 13)
        self._playersBid=[0,0,0,0]
        self._playersHandsWon=[0,0,0,0]
        self._playerScore=[0,0,0,0]

    def runRound(self):
        pass
        #returns self.getFinalScore

    def getFinalScore(self):
        return self._playersScore
