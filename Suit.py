from enum import Enum

class Suit(Enum):
    Hukum = 4
    Chidi = 2
    Itta = 3
    Paan  = 1

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        if self.value == 4:
            return '♠'
        elif self.value == 2:
            return '♣'
        elif self.value == 3:
            return '♦'
        return '♥'

if __name__ == '__main__':
    for suit in Suit:
        print(suit)
