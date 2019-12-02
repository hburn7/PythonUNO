import UnoCardModel
import GenerateDeck
import random

from random import shuffle
from itertools import product, repeat, chain
    
def create_uno_deck():
   COLORS = ['red', 'yellow', 'green', 'blue']
   NUMBERS = list(range(10)) + list(range(1, 10))
   COLORED_SPECIALS = ['skip', 'reverse', '+2']
   COLOR_CARD_TYPES = NUMBERS + COLORED_SPECIALS * 2
   WILD_CARD_TYPES = ['colorswap', '+4']
   color_cards = product(COLORS, COLOR_CARD_TYPES)
   wild_cards = product(repeat('wild', 4), WILD_CARD_TYPES)
   deck = list(chain(color_cards, wild_cards))
   shuffle(deck)
   return deck


def deal_one_card(p,deck):
    if len(deck)==0:
        return
    i = random.randint(0,len(deck)-1)
    p.cards.append(deck[i])
    deck.remove(deck[i])
def create_discard_pile(deck):
    discard_pile = []
    i = random.randint(0,len(deck)-1)
    discard_pile.append(deck[i])
    deck.remove(deck[i])
    return discard_pile
def deal(p1,p2,p3,p4,deck):
    for i in range(7):
        deal_one_card(p1,deck)
        deal_one_card(p2,deck)
        deal_one_card(p3,deck)
        deal_one_card(p4,deck)
        deal_one_card(p5,deck)
        deal_one_card(p6,deck)
        deal_one_card(p7,deck)
        deal_one_card(p8,deck)
            

p1 = Player("Marcus",1)
p2 = Player("Harry",2)
p3 = Player("Jordan",3)
p4 = Player("Franklin",4)
deck = create_uno_deck()
deal(p1,p2,p3,p4,deck)
discard_pile = create_discard_pile(deck)
print(p1)
print(p2)
print(p3)
print(p4)
print(discard_pile[-1])
