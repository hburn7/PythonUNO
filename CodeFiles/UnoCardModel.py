class UnoCard:
    color = None  # R, G, B, Y
    number = None  # Number 0-9 representing the card.
    special = None
    wild = None

    _card = None

    def __init__(self, c, n, s, w):
        self.color = c
        self.number = n
        self.special = s
        self.wild = w
        self._card = 'Card: {}{} Special: {} Wild? {}'.format(c, n, s, w)


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