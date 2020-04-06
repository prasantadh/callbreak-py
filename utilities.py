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