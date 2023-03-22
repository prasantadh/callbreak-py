from commons.Deck import Deck
from commons.Card import Card

from flask import Flask

class HighLow:
    def __init__(self) -> None:
        self.deck = Deck()
        self.score = 0
        self.app = Flask(__name__)

    def new(self):
        self.deck = Deck()
        return self.deck.deal()

    def last_dealt(self):
        return self.last_top()

    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value