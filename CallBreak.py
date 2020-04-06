from CardGame import CardGame

class CallBreak(CardGame):
    def __init__(self):
        super().init()

if __name__=='__main__':
    game = CardGame('CallBreak')
    print(game)
