from commons.Deck import Deck
from commons.Player import Player

from commons.exceptions.CallbreakExceptions import TooManyPlayersError

class CardGame(object):
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
        self.totalRoundsToPlay = 5
        self._scores = [] 
        self._current_round = 0
        self._players = []
        self.minPlayersAllowed = 1
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def players(self):
        return self._players

    @property
    def scores(self):
        return self._scores
    
    @property
    def calls(self):
        return self._calls

    def addPlayer(self, player: Player):
        id = len(self.players)
        if id >= self.maxPlayersAllowed:
            raise TooManyPlayersError

        print(id, len(self.calls), len(self.scores))
        player.id = len(self._players)

        self._scores.append([])
        player.scores = self.scores[id]

        self._calls.append([])
        player.calls = self.calls[id]

        self._players.append(player)

    def __str__(self):
        """
        __str__ _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return 'The {} game is on!'.format(self.name)
