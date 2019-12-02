class UnoCard:
    def __init__(self, color, card_type):
            self._validate(color, card_type)
            self.color = color
            self.card_type = card_type

    def _validate(self, color, card_type):
        if color not in ALL_COLORS:
            raise ValueError('Invalid color')
        if color == 'wild' and card_type not in WILD_CARD_TYPES:
            raise ValueError('Invalid card type')
        if color != 'wild' and card_type not in COLOR_CARD_TYPES:
            raise ValueError('Invalid card type')

COLORS = ['red', 'yellow', 'green', 'blue']
    ALL_COLORS = COLORS + ['wild']
    NUMBERS = list(range(10)) + list(range(1, 10))
    COLORED_SPECIALS = ['skip', 'reverse', '+2']
    COLOR_CARD_TYPES = NUMBERS + COLORED_SPECIALS * 2
    WILD_CARD_TYPES = ['colorswap', '+4']
    CARD_TYPES = NUMBERS + COLORED_SPECIALS + WILD_CARD_TYPES\

class DrawCard:
    amount = 0  # Amount of cards the player will draw when receiving this card (Will almost always be 2).
    color = ''

    def __init__(self, n, c):
        self.amount = n
        self.color = c


class ColoredSpecial:
    color = ''
    code = ''

    _card = color + ' ' + code

    def __init__(self, c, d):
        self.color = c
        self.code = d