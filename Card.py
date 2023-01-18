class Card:

    """Summary

    Attributes:
        faceRanks (dict): Description
        played (bool): Description
        rank (TYPE): Description
        suit (TYPE): Description
    """

    def __init__(self, suit, rank):
        """Summary

        Args:
            suit (TYPE): Description
            rank (TYPE): Description
        """
        self.suit = suit
        self.rank = rank
        self.faceRanks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
        self.played = False

    def __str__(self):
        """
        Returns string representation of Card.
        For a card that has already been played,
        it prints with a strikethrough, underline, and overline.

        Returns:
            str: string representation of current Card.
        """
        str_rep = self.suit + " " + self.rank

        if self.played:
            return '\u0305\u0332\u0336'.join(str_rep) + '\u0336\u0332\u0305'
        else:
            return str_rep

    def __repr__(self):
        """
        Creating a string representation of current Card.

        Returns:
            TYPE: String showing suit and rank. Example, ♠ 4.
        """
        return str(self)

    def __lt__(self, otherCard):
        """
        Overloads the < operator to make comparing cards possible.
        Comparison is based on rank of the card.

        Args:
            otherCard (Card): Another Card to compare with.

        Returns:
            Bool: Returns true if the rank of the other card
            is less than the rank of the current card.
        """
        return self.getRankValue() < otherCard.getRankValue()

    def __eq__(self, otherCard):
        """
        Overloads the equality (and inequality) operator.
        Allows to compare the ranks of two cards.

        Args:
            otherCard (Card): Another card to compare current card with.

        Returns:
            Bool: True if the ranks of self and otherCard are equal.
        """
        if isinstance(otherCard, Card):
            return self.getRankValue() == otherCard.getRankValue()
        return False

    def getRankValue(self):
        """
        Return the numeric (int) value of the rank of current card.

        Returns:
            int: Rank value of current card. J = 11; Q = 12; K = 13;
            A = 14;
        """
        if self.rank in self.faceRanks.keys():
            return self.faceRanks[self.rank]
        else:
            return int(self.rank)

if __name__=='__main__':
    # card = Card('Hukum-ko-','Ekka')
    print(card)

    print(Card('♠','A') == Card('♠','A'))
    print(Card('♠','J') < Card('♦','A'))
    print(Card('♣','5') < Card('♠','2'))
    print(Card('♠','A') != Card('♠','A'))
    print(Card('♠','A') != Card('♠','4'))

    print(Card('♠','4'))






