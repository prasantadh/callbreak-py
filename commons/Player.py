from callbreak.commons.Card import Card
from callbreak.commons.Hand import Hand


class Player:
    def __init__(self, name: str):
        """
        __init__ _summary_

        _extended_summary_

        Arguments:
            name -- _description_
        """
        self.name = name
        self.hand = Hand()
        self.score = 0
        self.cards = []
        self.soft_wrap = True

    def __str__(self) -> str:
        """
        __str__ _summary_

        _extended_summary_

        Returns:
            _description_
        """
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
