from commons.Deck import Deck
from commons.Card import Card

from flask import Flask

class HighLow:
    def __init__(self) -> None:
        self.deck = Deck()
        self.score = 0
        self.isOn = False

    def new(self):
        self.deck = Deck()
        self.isOn = True
        self.score = 0
        return self.deck.deal()

    def peek_next_card(self):
        return self.deck.top()
    
    def last_dealt(self):
        return self.deck.last_top()

    # returns true for correct guess
    # false otherwise
    def call(self, guess):
        print(self.last_dealt(), self.peek_next_card(), self.last_dealt() > self.peek_next_card())
        print(self.last_dealt(), self.peek_next_card(), self.last_dealt() < self.peek_next_card())
        if guess == 'high' and self.last_dealt() < self.peek_next_card():
            self.score += 1
            return True
        if guess == 'low' and self.last_dealt() > self.peek_next_card():
            self.score += 1
            return True

        self.isOn = False
        return False
    
    def deal(self):
        if self.isOn:
            card = self.deck.deal()
            if self.deck.empty():
                self.game.isOn = False
            return card

    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value

    @property
    def isOn(self) -> bool:
        return self._isOn
    
    @isOn.setter
    def isOn(self, value):
        self._isOn = value