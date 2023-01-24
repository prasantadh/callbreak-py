from rich.layout import Layout
from rich.panel import Panel


def sorting_card_keyy(x):
    """
    Returns a rank for a given card.
    This is based on suit and rankValue.

    Args:
        x (Card): Card whose rank is to be returned.

    Returns:
        int: Numeric value of the given card's rank.
    """
    suit_values = {'♠': 52, '♥': 39, '♣': 26, '♦': 13}
    return suit_values[x.suit] + x.getRankValue()


def render_empty_card(for_across_a_row: bool = True, color: str = "white", text: str = " ", width: int = 6, height: int = 4) -> Panel:
    """
    render_empty_card 
    Renders an empty card for "other" players.
    Esentially a flipped card.

    _extended_summary_

    Keyword Arguments:
        for_across_a_row -- whether the cards are to be
        printed across horizontally or veritcally (default: {True})
        color -- _description_ (default: {"white"})
        text -- any text we might want on the back of
        the card. Currently using random stuff like dragons
        and comets. (default: {" "})
        width: width of card
        heigh: height of card

    Returns:
        _description_
    """

    layout = Layout()
    if for_across_a_row:
        layout.split_column(
            Layout(text, name="upper"),
        )
    else:
        layout.split_row(
            Layout(text, name="upper")
        )

    return Panel(layout, width=width, height=height, style=color)