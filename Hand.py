class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ''.join(str(card)+' ' for card in self.cards).strip()

    def addCard(self, card):
        self.cards.append(card)

if __name__ == '__main__':
    hand = Hand()
    print(hand)
