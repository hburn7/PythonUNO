import UnoCardModel

class GenerateDeck:
    def genDeck():
        k = 0

        deck = []
        letters = ['R', 'G', 'B', 'Y', 'P']
        specialCardsColors = ['Draw 2', 'Reverse', 'Skip']

        for i in letters:
            for j in range(1, 10):
                deck.append(UnoCardModel.UnoCard(i, j, '', False))
                print(deck[k]._card)
                k += 1
        z = len(deck)
        for l in letters:
            for s in specialCardsColors:
                for y in range(2):
                    deck.append(UnoCardModel.UnoCard(l, None, s, False))
                    print(deck[z]._card)
                    z += 1
