from CardGame import CardGame

class CallBreak(CardGame):
    def __init__(self):
        super().init()
        self.totalRound=5
        self.currentRound=0
        self.numberOfPlayers=4

if __name__=='__main__':
    game = CardGame('CallBreak')
    print(game)
