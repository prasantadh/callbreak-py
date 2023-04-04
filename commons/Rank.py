from enum import Enum


class Rank(Enum):
    Ekka = 14
    Badshah = 13
    Missi = 12
    Ghulam = 11
    Dahar = 10
    Nahar = 9
    Attha = 8
    Satta = 7
    Chhakka = 6
    Panja = 5
    Chauka = 4
    Tirka = 3
    Dua = 2

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __repr__(self) -> str:
        if self.value < 11:
            return str(self.value)
        return ['J', 'Q', 'K', 'A'][self.value - 11]

    def __str__(self) -> str:
        return self.__repr__()

    def get_value(self):
        return self.value

    def get_alphabet_representation(self) -> str:
        """
        get_alphabet_representation
        This is same as str for 2-9 but for 10, J, Q, K, A, returns those
        characters to print them on screen.

        _extended_summary_

        Returns:
            alphabetical representation of card's rank
        """
        if self.get_value() < 10:
            return str(self.get_value())

        return ("T", "J", "Q", "K", "A")[self.get_value() - 10]
