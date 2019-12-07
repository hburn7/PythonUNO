def UNO():  
    import random  
    deck = []
    discard = []
    colors = ['Red','Blue','Green','Yellow']
    special = ['Draw 2','Skip','Reverse']

    for h in range(2):
        for i in colors:
            for j in range(1,10):
                card = i + ' ' + str(j)
                deck.append(card)

    for i in range(1):
        for j in colors:
            card = j + ' ' + str(0)
            deck.append(card)

    for i in range(2):
        for j in colors:
            for k in special:
                card = j + ' ' + k
                deck.append(card)

    for i in range(4):
        card = 'Wild'
        deck.append(card)
        card = 'Wild Draw 4'
        deck.append(card)

    #print(len(deck))

    while True:
        try:
            numPlayers = int(input('How many players will be playing? Please enter a value between 2 and 8: '))
            if 2 <= numPlayers <= 8:
                break
            print('Invalid number, please try again.')
        except ValueError:
            print("You have entered an invalid input. Please try again.")

    playerHands = {}

    for i in range(1,(numPlayers + 1)):
        playerHands['Player' + str(i)] = []
    #print(playerHands)

    random.shuffle(deck)

    # print(deck)

    for i in range(7):
        for j in range(1,len(playerHands) + 1):
            playerHands['Player' + str(j)].append(deck[0])
            del deck[0]
    
    # print(playerHands)
    # print(len(deck))
    
    count = 1
    direction = 1
    discard.append(deck[0])
    deck.remove(deck[0])
    print(discard[0])

    while count <= (len(playerHands)):
        print('Player' + str(count) + "'s hand: ", playerHands['Player' + str(count)])
        index_of_card = ((int(input('Player %s, what number card would you like to play? ' % str(count)))) - 1)
        
        playerHand = playerHands['Player' + str(count)]
        card = playerHand[index_of_card]

        PlayCard(playerHand, index_of_card, card, discard)
        drawnCard = deck[0]
        if(CardIsNotMatch(discard, card)):
            DrawCard(deck, playerHand) # MAKE THEM DRAW HERE
            if CardIsNotMatch(discard, drawnCard):
                continue
            if CardIsMatch(discard, drawnCard):
                print('Player' + str(count) + "'s hand: ", playerHands['Player' + str(count)])
                index_of_card = ((int(input('Player %s, what number card would you like to play? ' % str(count)))) - 1)
        
                playerHand = playerHands['Player' + str(count)]
                card = playerHand[index_of_card]

                PlayCard(playerHand, index_of_card, card, discard)

        if len(playerHands['Player' + str(count)]) == 0:
            print('Player' + str(count) + ' wins!')
            count = 9
        if direction == 1:                                  # THIS IS WHERE I PUT THE SKIP AND REVERSE - JORDAN
            if direction == 1 and card[-7:] == 'Reverse':
                direction = 2
                count = count - 1
                continue
            if direction == 1 and card[-4:] == 'Skip':
                count = count + 2
            else:
                count = count + 1
                
        if direction == 2:
            if direction == 2 and card[-7:] == 'Reverse':
                direction = 1
                count = count + 1
                continue
            if direction == 2 and card[-4:] == 'Skip':
                count = count - 2
            else:
                count = count - 1             
        if count == (len(playerHands) + 1):
           count = 1
        if count < 1:
            count = len(playerHands)
def ReplayPrompt(playerHand, discard, card):
    j = 0
    for i in range(1, len(playerHand)):
        if(CardIsNotMatch(discard, playerHand[i])):
            j = j + 1
    if(j == len(playerHand)):
        print('You do not have a playable card. Skipping turn...')
        
def PlayCard(playerHand, index_of_card, card, discard):
    if(CardIsMatch(discard, card)):
        discard.append(card)
        del playerHand[index_of_card]
        print('Discard Pile: ', discard[-1])
    else:
        print('Hey, did you forget the rules?! This card is not playable. Please try again.')


def CardIsNotWild(card):
    if(card[0] != 'W'):
        return True
    return False

def CardIsWild(card):
    if(card[0] == 'W'):
        return True
    return False

def CardIsNotMatch(discard, card):
    if(discard[-1][0] != card[0] and
        discard[-1].split(' ')[1] != card.split(' ')[1] and CardIsNotWild(card)):
        return True
    return False

def CardIsMatch(discard, card):
    if(discard[-1][0] == card[0] or
        discard[-1].split(' ')[1] == card.split(' ')[1] or CardIsWild(card)):
        return True
    return False

def DrawCard(deck, playerHand):
    playerHand.append(deck[0])
    del deck[0]



UNO()