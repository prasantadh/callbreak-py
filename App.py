from callbreak.CallBreak import CallBreak
from commons.Player import Player


import logging





players = [Player('1'), Player('2'), Player('3'), Player('4')]

game = CallBreak()
for player in players:
    game.addPlayer(player)
game.play()

game.render("http://127.0.0.1:5000/")
