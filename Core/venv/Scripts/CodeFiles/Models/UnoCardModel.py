class UnoCard:
    color = ''  # R, G, B, Y
    number = 0  # Number 0-9 representing the card.
    special = ''  # Here we can put something like D4 for Draw 4, CC for color change, S for skip.

    def __init__(self, c, n, s):
        self.color = c
        self.number = n
        self.special = s
