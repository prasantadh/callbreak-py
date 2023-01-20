from Hand import Hand
from Card import Card


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

    def getCards(self) -> list[Card]:
        """
        getCards _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return self.cards

    def sortCards(self, ascending: bool = True):
        """
        sortCards _summary_

        _extended_summary_

        Keyword Arguments:
            ascending -- _description_ (default: {True})
        """
        self.cards = sorted(self.cards, key=lambda card: (card.suit.value, card.rank.value), reverse=not ascending)


# play hand
# number of winning hands
#

if __name__ == '__main__':
    player = Player('Player 1')
    print(player)
