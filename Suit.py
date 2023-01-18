from enum import Enum

Suit = Enum('Suit', ['HUKUM', 'CHIDI', 'ITTA', 'PAAN'])

class Suit(Enum):
    HUKUM = '♠'
    CHIDI = '♣'
    ITTA  = '♦'
    PAAN  = '♥'

    def __lt__(self, other):
        return self.value == '♠' and other.value != '♠'

if __name__ == '__main__':
    for suit in Suit:
        print(suit)
