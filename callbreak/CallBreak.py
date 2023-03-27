from commons.CardGame import CardGame
from commons.Player import Player
import json

class CallBreak(CardGame):

    def __init__(self):
        super().__init__(name='CallBreak')
        self.maxPlayersAllowed = 4
        self.minPlayersAllowed = 4
        self._numberOfPlayers = 0
        self.isOn = False
        self._calls = []


    def new(self):
        self.isOn = True
        self._current_round = 0
        self._numberOfPlayers = 0
        self._players = []
        # code to initialize the new game
    
    @property
    def current_round(self):
        return self.current_round
    
    @current_round.setter
    def current_round(self, value):
        self.current_round = value


    @property
    def player_names(self):
        return [player.name for player in self.players]