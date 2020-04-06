from Haat import Haat

class Round:

    def __init__(self, orderdPlayers, deck):
        self.players=orderedPlayers #first player starts the round
        self.shuffledDeck=deck
        self.totalPlays=13
        self._playersBid=[0,0,0,0]
        self._playersHandsWon=[0,0,0,0]
        self._playerScore=[0,0,0,0]

    def runRound(self):
        for i in range(0, self.totalPlays):
            # initialize play, set it to self.currentPlay
            # run Play
            #
            self.currentPlayNum+=1
        pass
        #returns self.getFinalScore

    def getFinalScore(self):
        return self._playersScore
