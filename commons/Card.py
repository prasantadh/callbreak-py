from commons.Rank import Rank
from commons.Suit import Suit

class Card:

    def __init__(self, suit: Suit, rank: Rank):
        """
        Arguments:
            suit -- Card's suit (Hukkum, Paan, ...)
            rank -- Card's rank (A, 2, 3, ...)
        """
        self.suit = suit
        self.rank = rank

        self.faceRanks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
        self.played = False

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        """
        Creating a string representation of current Card.

        Returns:
            TYPE: String showing suit and rank. Example, ♠ 4.
        """
        return "{} {}".format(self.suit, self.rank)

    def __lt__(self, otherCard) -> bool:
        """
        Overloads the < operator to make comparing cards possible.
        Comparison is based on rank of the card.

        Args:
            otherCard (Card): Another Card to compare with.

        Returns:
            Bool: Returns true if the rank of the other card
            is less than the rank of the current card.
        """
        if self.suit == otherCard.suit: 
            return self.rank < otherCard.rank

        return False
    
    def __gt__(self, otherCard) -> bool:
        return not self < otherCard

    def __eq__(self, otherCard) -> bool:
        """
        Overloads the equality (and inequality) operator.
        Allows to compare the ranks of two cards.

        Args:
            otherCard (Card): Another card to compare current card with.

        Returns:
            Bool: True if the ranks of self and otherCard are equal.
        """
        if isinstance(otherCard, Card):
            return self.suit == otherCard.suit and self.rank == otherCard.rank
        return False

    def getRankValue(self) -> int:
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


    def get_suit(self) -> Suit:
        """
        get_suit _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return self.suit

    def get_rank(self) -> Rank:
        """
        get_rank _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return self.rank
