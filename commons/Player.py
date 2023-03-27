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
        self._scores = []
        self._calls = []
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    def call(self, value):
        self._calls.append(value)

    @property 
    def calls(self):
        return self._calls
    
    @calls.setter
    def calls(self, value):
        self._calls = value
    
    def score(self, value):
        return self._scores.append(value)
    
    @property
    def scores(self, value):
        return self._scores

    @scores.setter
    def scores(self, value):
        self._scores = value


    def __str__(self) -> str:
        return "{} : {}".format(self.name, self.cards)

    def addCard(self, card: Card):
        """
        addCard _summary_

        _extended_summary_

        Arguments:
            card -- _description_
        """
        self.cards.append(card)

    def getNumberOfRemainingCards(self) -> bool:
        """
        getNumberOfRemainingCards Return the number of yet-unplayed cards.

        _extended_summary_

        Returns:
            Numbre of cards that haven't been played yet.
        """
        return sum([not card.played for card in self.cards])

    def setHand(self, hand: Hand):
        """
        setHand _summary_

        _extended_summary_

        Arguments:
            hand -- _description_
        """
        self.hand = hand

    def getHand(self) -> Hand:
        """
        getHand _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return self.hand

    def getCards(self):
        """
        getCards _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return self.cards


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
        self.cards = sorted([card for card in self.cards if not card.played], key=lambda card: (card.suit.value, card.rank.value), reverse=not ascending)
