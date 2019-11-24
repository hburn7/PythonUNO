class UnoCard:
    color = ''  # R, G, B, Y
    number = 0  # Number 0-9 representing the card.
    special = ''  # R or S for reverse and skip respectively.

    def __init__(self, c, n, s):
        self.color = c
        self.number = n
        self.special = s


class DrawCard:
    amount = 0  # Amount of cards the player will draw when receiving this card (Will almost always be 2).
    color = ''

    def __init__(self, n, c):
        self.amount = n
        self.color = c


class OtherSpecial:
    type = ''

    def __init__(self, t):
        self.type = t
