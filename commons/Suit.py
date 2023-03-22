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
        if self.value == self.Hukum and other.value != self.Hukum:
            return False
        if self.value != self.Hukum and other.value == self.Hukum:
            return True
        # this part means the a < b and b < a can both return False
        # if they are both not Hukum. this is because in the game,
        # the first card to be played is greater. 
        # keep this in mind when comparing cards later
        return False
    
    def __eq__(self, other) -> bool:
        if self.value == other.value:
            return True

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.__repr__()