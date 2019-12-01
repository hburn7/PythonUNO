# NOTE: 

class UnoCard:
    color = ''  # R, G, B, Y
    number = 0  # Number 0-9 representing the card.
    special = ''  # R or S for reverse and skip respectively.

    def __init__(self, color, num, special):
        self.color = color
        self.number = num
        self.special = special

class UnoCardSpecial:
    color = '' # R, G, B, Y
    special = '' # D4W, D2, W, R, S

    def __init__(self, color, specialModifier):
        self.color = color
        self.special = specialModifier

class Main:
    print('Welcome to Harry, Jordan, and Frankie\'s Python UNO!')

    # We use while True because if someone puts in a wrong input they will now be re-prompted.
    while True:
        try:
            numPlayers = int(input('How many players will be playing? Please enter a value between 2 and 8: '))
            if 2 <= numPlayers <= 8:
                break
            print('Invalid number, please try again.')
        except ValueError:
            print("You have entered an invalid input. Please try again.")