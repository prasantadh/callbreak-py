from commons.Suit import Suit
from commons.Rank import Rank
from commons.Card import Card

import json
import os
import requests

def get_suit(s):
    # The server sends the string representation of each suit
    # Make sure to compare the value against the same
    for suit in Suit:
        if str(suit) == s:
            return suit
    
def get_rank(r):
    # The server sends the string representation of each rank
    # Make sure to compare the value against the same
    for rank in Rank:
        if str(rank) == r:
            return rank

class Client:
    def __init__(self, server='http://127.0.0.1:5000') -> None:
        self.cards = []
        self.server = server
        self.score = 0
        
    def new(self) -> bool:
        try:
            response = requests.get(self.server + '/new')
        except Exception as E:
            print(E)
            print("Fatal Error: Couldn't establish connection with the server!")
            exit()
        
        response = json.loads(response.text)
        if response['result'] == 'failure':
            print('Server reported error: {}'.format(response['data']['reason']))
            return False

        self.score = response['data']['score']
        
        suit = get_suit(response['data']['card'][0])
        rank = get_rank(response['data']['card'][1:])
        self.cards.append(Card(suit=suit, rank=rank))
    
    def __repr__(self) -> str:
        return ''.join(str(card) + '\n' for card in self.cards)

    def send(self, value):
        payload = {'data' : {'guess' : 'high'} }
        response = requests.post(self.server + '/call', json=payload)
        
    def run(self):
        self.new()
        print(self)
        for i in range(51):
            guess = input('High [H/h: default] or Low [l]? ')
            if guess.lower() in ['h', 'high', '']:
                self.send('high')
            else:
                self.send('low')
            print('-'*20)
            print(self)