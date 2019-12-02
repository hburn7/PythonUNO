import UnoCardModel

class GenerateDeck:
    from random import shuffle
    from itertools import product, repeat, chain

    COLORS = ['red', 'yellow', 'green', 'blue']
    ALL_COLORS = COLORS + ['wild']
    NUMBERS = list(range(10)) + list(range(1, 10))
    COLORED_SPECIALS = ['skip', 'reverse', '+2']
    COLOR_CARD_TYPES = NUMBERS + COLORED_SPECIALS * 2
    WILD_CARD_TYPES = ['colorswap', '+4']
    CARD_TYPES = NUMBERS + COLORED_SPECIALS + WILD_CARD_TYPES

    def create_uno_deck():
        color_cards = product(COLORS, COLOR_CARD_TYPES)
        wild_cards = product(repeat('wild', 4), WILD_CARD_TYPES)
        deck = list(chain(color_cards, wild_cards))
        shuffle(deck)
        return deck

    #The_Deck = create_uno_deck()
    #print(The_Deck)


#from random import shuffle
#from itertools import product, repeat, chain
#
#COLORS = ['red', 'yellow', 'green', 'blue']
#ALL_COLORS = COLORS + ['wild']
#NUMBERS = list(range(10)) + list(range(1, 10))
#COLORED_SPECIALS = ['skip', 'reverse', '+2']
#COLOR_CARD_TYPES = NUMBERS + COLORED_SPECIALS * 2
#WILD_CARD_TYPES = ['colorswap', '+4']
#CARD_TYPES = NUMBERS + COLORED_SPECIALS + WILD_CARD_TYPES

#def create_uno_deck():
#color_cards = product(COLORS, COLOR_CARD_TYPES)
#wild_cards = product(repeat('wild', 4), WILD_CARD_TYPES)
#deck = list(chain(color_cards, wild_cards))
#shuffle(deck)
#return deck

#The_Deck = create_uno_deck()
#print(The_Deck)
