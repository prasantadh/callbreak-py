from enum import Enum

class Suit(Enum):
    """
    Suit _summary_

    _extended_summary_

    Arguments:
        Enum -- _description_

    Raises:
        Exception: _description_

    Returns:
        _description_
    """

    Hukum = '♠'
    Chidi = '♣'
    Itta = '♦'
    Paan = '♥'

    def __lt__(self, other) -> bool:
        """
        __lt__ _summary_

        _extended_summary_

        Arguments:
            other -- _description_

        Returns:
            _description_
        """
        if self.value == self.Hukum.value and other.value != self.Hukum.value:
            return False
        if self.value != self.Hukum.value and other.value == self.Hukum.value:
            return True
        # this part means the order of comparison matters
        # if both the suits aren't Hukum, the first card
        # that was dropped wins
        return False

    def __gt__(self, other) -> bool:
        return not self < other
    
    def __eq__(self, other) -> bool:
        if self.value == other.value:
            return True

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.__repr__()