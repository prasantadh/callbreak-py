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

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        if self.value == 14:
            return 'A'
        elif self.value == 13:
            return 'K'
        elif self.value == 12:
            return 'Q'
        elif self.value == 11:
            return 'J'
        else:
            return str(self.value)

if __name__=='__main__':
    for rank in Rank:
        print(rank)

