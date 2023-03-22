from commons.Deck import Deck
from commons.Card import Card

from flask import Flask

class HighLow:
    def __init__(self) -> None:
        self.deck = Deck()
        self.score = 0

    def new(self):
        self.deck = Deck()
        return self.deck.deal()

    def next_card(self):
        return self.deck.top()
    
    def last_dealt(self):
        return self.deck.last_top()

    def call(self, guess):
        if guess == 'high' and self.next_card() > self.last_dealt():
            self.score += 1
            return True
        if self.next_card() < self.last_dealt():
            self.score += 1
            return True
        else:
            return False
    
    def deal(self):
        return self.deck.deal()

    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value