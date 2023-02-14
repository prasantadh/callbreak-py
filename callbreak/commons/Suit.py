from enum import Enum

suit_colors = ["\x1b[30m", "\x1b[31m"]   # Gray (for black) & red.
color_str_terminal_char = "\x1b[0m"


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
    Hukum = 4
    Chidi = 2
    Itta = 3
    Paan = 1

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

    def __str__(self) -> str:
        if self.value == 4:
            s = '♠'
        elif self.value == 3:
            s = '♦'
        elif self.value == 2:
            s = '♣'
        elif self.value == 1:
            s = '♥'
        else:
            raise Exception("ERROR: Unknown suite given.")

        return f"{suit_colors[self.value % 2]}{s}{color_str_terminal_char}"


    def get_descriptive_name(self) -> str:
        """
        get_descriptive_name _summary_

        _extended_summary_

        Raises:
            Exception: _description_

        Returns:
            _description_
        """
        if self.value == 4:
            s = 'spade'
        elif self.value == 3:
            s = 'diamond'
        elif self.value == 2:
            s = 'club'
        elif self.value == 1:
            s = 'heart'
        else:
            raise Exception("ERROR: Unknown suite given.")

        return s


    def get_value(self) -> int:
        return self.value


if __name__ == '__main__':
    for suit in Suit:
        print(suit)
