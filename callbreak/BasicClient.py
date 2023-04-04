from commons.Card import Card
from commons.Hand import Hand
from commons.Rank import Rank
from commons.Suit import Suit

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
        self._hand = None
        self.server = server
        self.score = 0

    @property
    def hand(self):
        return self._hand

        
    def parseHand(self, response):
        response = json.loads(response.text)
        if response['result'] == 'failure':
            print('Server reported error: {}'.format(response['data']['reason']))
            exit()

        self._hand = Hand()
        cards = response['data']['cards'].split(',')
        for card in cards:
            suit = get_suit(card[0])
            rank = get_rank(card[2:])
            self._hand.add(Card(suit=suit, rank=rank))

    def new(self) -> bool:
        try:
            response = requests.get(self.server + '/new/prasant')
        except Exception as E:
            print(E)
            print("Fatal Error: Couldn't establish connection with the server!")
            exit()


    def call(self, value) -> bool:
        response = requests.get(self.server + f'/call/{value}')
    

    def __repr__(self) -> str:
        s = ''.join(str(card) + '\n' for card in self.cards)
        s += 'score: {}'.format(self.score)
        return s

    def send(self, value):
        payload = {'data' : {'guess' : value} }
        response = requests.post(self.server + '/call', json=payload)
        return response

    def getHand(self, round=0):
        payload = {
            'data' : {
                'round' : round,
                'player' : 0,
                'break' :  0
            }
        } 
        response =  requests.get(self.server + '/status')
        self.parseHand(response)


    def render(self):
        self._hand.sort()
        print(self.hand)


    def play(self, i):
        pass

        
    def run(self):
        self.new()
        for round in range(5):
            self.getHand()
            self.render()
            # self.call(1)
            for trick in range(13):
                self.play(0)

        response = requests.get(self.server + '/status')
        print(response.text)

        # for i in range(51):
        #     guess = input('High [H/h: default] or Low [l]? ')
        #     if guess.lower() in ['h', 'high', '']:
        #         response = self.send('high')
        #     else:
        #         response = self.send('low')
        #     suit, rank = self.parse_response(response)
        #     self.cards.append(Card(suit, rank))
        #     print('-'*20)
        #     print(self)