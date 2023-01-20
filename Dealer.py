from Deck import Deck
from Hand import Hand
from CallBreak import CallBreak


class Dealer:
    def __init__(self):
        """
        __init__ _summary_

        _extended_summary_
        """
        self.deck = Deck()
        self.hands = [Hand(), Hand(), Hand(), Hand()]

    def deal(self, game: CallBreak):
        """
        deal _summary_

        _extended_summary_

        Arguments:
            game -- _description_

        Returns:
            _description_
        """
        self.deck.shuffle()
        for cardPosition in range(00, 13): self.hands[0].addCard(self.deck[cardPosition])
        for cardPosition in range(13, 26): self.hands[1].addCard(self.deck[cardPosition])
        for cardPosition in range(26, 39): self.hands[2].addCard(self.deck[cardPosition])
        for cardPosition in range(39, 52): self.hands[3].addCard(self.deck[cardPosition])
        return self.hands


if __name__ == '__main__':
    dealer = Dealer()
    dealer.deal(CallBreak())
    for hand in dealer.hands:
        print(hand)