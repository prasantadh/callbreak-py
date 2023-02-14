from callbreak.commons.Rank import Rank
from callbreak.commons.Suit import Suit
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align

from rich import print
from rich.padding import Padding

class Card:

    """
     _summary_

    _extended_summary_
    """

    def __init__(self, suit: Suit, rank: Rank):
        """
        __init__ _summary_

        _extended_summary_

        Arguments:
            suit -- Card's suit (Hukkum, Paan, ...)
            rank -- Card's rank (A, 2, 3, ...)
        """
        self.suit = suit
        self.rank = rank

        self.faceRanks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
        self.played = False
        # This is for coloring the text representations of each card's suit.
        self.suit_colors = ["\x1b[37m", "\x1b[31m"]   # Gray (for black) & red.

    def __str__(self) -> str:
        """
        Returns string representation of Card. Uses suit_colors
        to figure out the color (red vs black/gray).
        For a card that has already been played,
        it prints with a strikethrough, underline, and overline.

        Returns:
            str: string representation of current Card.
        """
        return f"{self.suit.get_descriptive_name()} {self.rank.get_alphabet_representation()}"

    def emojified_rep(self) -> str:
        """
        emojified_rep Returns a string representation where the suit is a
        Unicode emoji. This just looks nicer- that's all.

        _extended_summary_

        Returns:
            str: string representation where suits are represented by the
            coresponding emojis.
        """
        # The first element is empty because we 1-count the
        # suit values.
        suit = ["", ":heart_suit-emoji:", ":club_suit-emoji:", ":diamond_suit-emoji:", ":spade_suit-emoji:"][self.suit.value]
        # This is same as str for 2-9 but for 10, J, Q, K, A, returns those
        # characters.
        rank = self.rank.get_alphabet_representation()
        # This is required because we represent 10 as T
        # in face_values in the render_fancy() method below.
        # Enables to use a single string to define all ranks instead of a
        # list with 13 values.
        if rank == "T":
            rank = "10"
        return "{}\n{}".format(suit, rank)

    def __repr__(self) -> str:
        """
        Creating a string representation of current Card.

        Returns:
            TYPE: String showing suit and rank. Example, ♠ 4.
        """
        str_rep = "{} {}".format(self.suit, self.rank.value)
        # Red if 0, 2. Black if 1, 3.
        color_str = self.suit_colors[((self.suit.get_value() - 1) % 2) == 0]
        color_str_terminal_char = "\x1b[0m"

        if self.played:
            # Unicode characters for strikethrough, underline, and overline.
            return '\u0305\u0332\u0336'.join(str_rep) + '\u0336\u0332\u0305'
        else:
            return f"{color_str}{str_rep}{color_str_terminal_char}"

    def __lt__(self, otherCard) -> bool:
        """
        Overloads the < operator to make comparing cards possible.
        Comparison is based on rank of the card.

        Args:
            otherCard (Card): Another Card to compare with.

        Returns:
            Bool: Returns true if the rank of the other card
            is less than the rank of the current card.
        """
        return self.getRankValue() < otherCard.getRankValue()

    def __eq__(self, otherCard) -> bool:
        """
        Overloads the equality (and inequality) operator.
        Allows to compare the ranks of two cards.

        Args:
            otherCard (Card): Another card to compare current card with.

        Returns:
            Bool: True if the ranks of self and otherCard are equal.
        """
        if isinstance(otherCard, Card):
            return self.getRankValue() == otherCard.getRankValue()
        return False

    def getRankValue(self) -> int:
        """
        Return the numeric (int) value of the rank of current card.

        Returns:
            int: Rank value of current card. J = 11; Q = 12; K = 13;
            A = 14;
        """
        if self.rank in self.faceRanks.keys():
            return self.faceRanks[self.rank]
        else:
            return int(self.rank)


    def get_suit(self) -> Suit:
        """
        get_suit _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return self.suit

    def render_fancy(self, color: bool = True) -> str:
        """
        render_fancy
        This returns single unicode characters where each
        character shows both the rank and suit defined here:
        https://unicode-table.com/en/blocks/playing-cards/

        For example, 🃑 instead of ♣ A.

        Requires smaller space particularly when the font size is
        normal to large.

        _extended_summary_

        Keyword Arguments:
            color -- Whether to color the representations
            red for diamond & hearts and black for the other two
             (default: {True})

        Returns:
            "Fancy" string representation with optional color.
        """
        # The very first character is a throw-away character.
        # This is needed because of 0 vs 1 counting.
        face_values = 'BA23456789TJCQK'
        # Offsets for unicode of specific cards from their respective bases.
        # 🂡 is U+1F0A1, 🂢 is U+1F0A2 and so on.
        # Tells us what to add to the base unicode values to obtain the correct
        # card.
        unicode_for_face = '0123456789ABCDE'
        # Unicode is spade, hearts, diamond, clubs. Our is hearts, club, diamond, spade. [1, 3, 2, 0]
        unicode_for_suit = 'BDCA'

        current_rank = self.rank.get_alphabet_representation()
        # 0 vs 1 counting.
        unicode_str = f"0001f0{unicode_for_suit[self.suit.get_value() - 1]}"\
            f"{unicode_for_face[face_values.index(str(current_rank))]}"

        # Red if 0, 2. Black if 1, 3.
        color_str = self.suit_colors[((self.suit.get_value() - 1) % 2) == 0]
        # To make sure the coloring stops.
        color_str_terminal_char = "\x1b[0m"

        card_rep = (chr(int(unicode_str, base=16)))

        return f"{color_str}{card_rep}{color_str_terminal_char}"

    def get_rank(self) -> Rank:
        """
        get_rank _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return self.rank

    def rich_render(self, up: bool = False) -> Panel:
        """
        rich_render
        Uses the rich library to produce "rich"
        representations for cards where we basically draw
        a rectangle with suit and rank to make a card.
        This produces cards that are much bigger than a single unicode
        character cards which can be difficult to see.

        _extended_summary_

        Returns:
            A rich Panel object that's basically a drawing of the
            current card.
        """

        # Use a table to draw the card.
        table = Table(title="",
                            show_lines=False,
                            show_header=False,
                            expand=True
                    )

        table.add_column("X", justify="right", style="cyan", no_wrap=False)

        # Want the card to be empty for now.
        table.add_row("")

        layout = Layout()

        text = self.emojified_rep()

        # To make the cards not too big, split the rank
        # and suit into two rows.
        layout.split_column(
            Layout(Align.center(text.split()[0]), name="upper"),
            Layout(Align.center(" "), name="middle"),
            Layout(Align.center(text.split()[1]), name="lower"),
        )

        layout['upper'].size = 1

        if up:
            pad = 0
        else:
            pad = 1

        return Padding(Panel(layout, width=8, height=6), (pad, 0, 0, 0), expand=False)


if __name__ == '__main__':

    card = Card(Suit.Paan, Rank.Dahar)
    print(card.rich_render(False))
