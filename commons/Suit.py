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
        return self.value < other.value

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.__repr__()

if __name__ == '__main__':
    for suit in Suit:
        print(suit)
