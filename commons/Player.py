from commons.Card import Card
from commons.Hand import Hand


class Player:
    def __init__(self, name: str, game):
        """
        __init__ _summary_

        _extended_summary_

        Arguments:
            name -- _description_
        """
        self.name = name
        self.id = 0
        self.cards = []
        self.soft_wrap = True
        self.game = game
        self._cards = []
        self._hands = []
        self._scores = []
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    # make a call() for the round
    def call(self, value: int):
        self._calls.append(value)

    # _calls is an array that has the player's calls
    # indexed by round 0-4 
    @property 
    def calls(self):
        return self._calls
    
    @calls.setter
    def calls(self, value):
        self._calls = value
    
    # player just scored a Trick
    def score(self, value):
        if len(self._scores) <= self.game.current_round:
            self._scores.append(0)
        self._scores[-1] += 1
    
    # _scores is an array that has the player's scores
    # indexed by round 0-4
    @property
    def scores(self, value):
        return self._scores

    @scores.setter
    def scores(self, value):
        self._scores = value


    def __str__(self) -> str:
        return "{} : {}".format(self.name, self.cards)

    def buy(self, card: Card) -> None:
        if len(self.hands) == self.game.currentRound:
            self._hands.append(Hand())
        self._hands[-1].add(card)
    
    @property
    def hands(self):
        return self._hands

    @hands.setter
    def hands(self, value):
        self._hands = value

    def getNumberOfRemainingCards(self) -> bool:
        """
        getNumberOfRemainingCards Return the number of yet-unplayed cards.

        _extended_summary_

        Returns:
            Numbre of cards that haven't been played yet.
        """
        return sum([not card.played for card in self.cards])

    def getCardFromIndex(self, index: int) -> Card:
        """
        getCardFromIndex _summary_

        _extended_summary_

        Arguments:
            index -- _description_

        Returns:
            _description_
        """
        return self.cards[index]

    def sortCards(self, ascending: bool = True):
        """
        sortCards _summary_

        _extended_summary_

        Keyword Arguments:
            ascending -- _description_ (default: {True})
        """
        self.cards = sorted([card for card in self.cards if not card.played], 
                            key=lambda card: (card.suit.value, card.rank.value), 
                            reverse=not ascending)
