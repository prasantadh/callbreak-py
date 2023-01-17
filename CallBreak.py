from CardGame import CardGame

class CallBreak(CardGame):
    numberOfPlayers = 4

    def __init__(self):
        super().__init__(name='CallBreak')
        self.totalRound=5
        self.currentRound=0

    def play(self):
        # for total number of rounds
        #   scores = Round.play()
        #   process the scores
        # endgame
        pass

if __name__=='__main__':
    game = CallBreak()
    print(game)
