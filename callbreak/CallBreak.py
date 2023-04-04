from commons.CardGame import CardGame
from commons.Deck import Deck
from commons.Player import Player
import json

class CallBreak(CardGame):

    def __init__(self):
        super().__init__(name='CallBreak')
        self.maxPlayersAllowed = 4
        self.minPlayersAllowed = 4
        self._numberOfPlayers = 0
        self.isOn = False


    def new(self):
        super().__init__(name='CallBreak')
        self.isOn = True
    

    @property
    def player_names(self):
        return [player.name for player in self.players]
    

    def deal(self):
        deck = Deck()
        i = 0
        while not deck.empty():
            self.players[i % 4].buy(deck.deal())
            i += 1

