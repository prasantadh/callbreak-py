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
    Paan = '♥'
    Chidi = '♣'
    Itta = '♦'

    def __lt__(self, other) -> bool:
        """
        __lt__ _summary_

        _extended_summary_

        Arguments:
            other -- _description_

        Returns:
            _description_
        """
        if self.value != other.value and other.value == self.Hukum.value:
            return True
        return False

    def __gt__(self, other) -> bool:
        if self.value == other.value:
            return False
        if other.value == self.Hukum.value:
            return False
        return True
    
    def __eq__(self, other) -> bool:
        if self.value == other.value:
            return True

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.__repr__()