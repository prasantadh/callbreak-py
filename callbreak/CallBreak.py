from commons.CardGame import CardGame
from commons.Player import Player
import json

class CallBreak(CardGame):

    def __init__(self):
        super().__init__(name='CallBreak')
        self.totalRound = 5
        self.round = 0
        self.maxPlayersAllowed = 4
        self.minPlayersAllowed = 4
        self.numberOfPlayers = 0
        self.isOn = False


    def new(self):
        self.isOn = True
        # code to initialize the new game
    
    @property
    def round(self):
        return self._round
    
    @round.setter
    def round(self, value):
        self._round = value
    

    def play(self):
        if len(self.players) != self.minPlayersAllowed:
            return False

        while not self.deck.empty():
            for player in self.players:
                player.addCard(self.deck.deal())

    def status(self):

        current_hand = ([str(c) for c in self.players[0].cards])

        status = { 'data' :
                    { 'hand' : json.dumps(current_hand) }
                  }
        return status

    def respond_success(self):
        return {
            'result' : 'success',
            'data' : {
                'hello'
            }
        }
    
    def respond_failure(self, message):
        return {
            'result' : 'failure',
            'data' : {
                'reason' : message
            }
        }