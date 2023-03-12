from callbreak.commons.Deck import Deck
from callbreak.commons.Player import Player
from Renderer import Renderer


class CardGame:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, numberOfRounds: int = 1, name: str = 'generic'):
        """
        __init__ _summary_

        _extended_summary_

        Keyword Arguments:
            numberOfRounds -- _description_ (default: {1})
            name -- _description_ (default: {'generic'})
        """
        self.name = name
        self.players = []   # TODO: Assume self.players[0] one is always self?
        self.numberOfPlayers = 1
        self.maxPlayersAllowed = 4
        self.minPlayersAllowed = 1
        self.numberOfRounds = numberOfRounds
        self.deck = Deck()
        self.renderer = Renderer()

    def addPlayer(self, player: Player):
        """
        addPlayer _summary_

        _extended_summary_

        Arguments:
            player -- _description_
        """
        if (len(self.players)) == self.maxPlayersAllowed:
            return False
        self.players.append(player)

    def __str__(self):
        """
        __str__ _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return 'The {} game is on!'.format(self.name)

    def render(self, server_address: str=""):
        print("Rendering")
        self.renderer.update_players(self.players)
        # self.renderer.render_call_break()
        self.renderer.render_live(server_address)

    def status(self):
        pass


if __name__ == '__main__':
    game = CardGame()
    print(game)
