from CardGame import CardGame

class CallBreak(CardGame):
    numberOfPlayers = 4

    def __init__(self):
        super().__init__('CallBreak')
        self.totalRound=5
        self.currentRound=0

if __name__=='__main__':
    game = CardGame('CallBreak')
    print(game)
