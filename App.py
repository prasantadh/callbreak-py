from callbreak.CallBreak import CallBreak
from callbreak.commons.Player import Player

players = [Player('1'), Player('2'), Player('3'), Player('4')]

game = CallBreak()
for player in players:
    game.addPlayer(player)
game.play()

game.render()
