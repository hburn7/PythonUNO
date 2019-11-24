from enum import Enum


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


# An Enum basically assigns a handy name to an integer. This way,
# we can call the class and say OtherSpecial.DRAWFOUR instead of another
# less easy-to-read naming scheme.

class OtherSpecial(Enum):
    COLORWHEEL = 1
    DRAWFOUR = 2  # We need to account for the color change when someone draws 4.
