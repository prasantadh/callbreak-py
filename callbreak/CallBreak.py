from callbreak.commons.CardGame import CardGame
from callbreak.commons.Player import Player
import json

class CallBreak(CardGame):

    def __init__(self):
        super().__init__(name='CallBreak')
        self.totalRound = 5
        self.currentRound = 0
        self.maxPlayersAllowed = 4
        self.minPlayersAllowed = 4

        # for now add 3 players so that we only wait for one to join
        for player_idx in range(3):
            self.addPlayer(Player(str(player_idx)))

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

if __name__ == '__main__':
    game = CallBreak()
    game.play()
    print(game.status())
    print(game)
