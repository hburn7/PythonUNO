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

    player_hands = {}

    for i in range(1,(numPlayers + 1)):
        player_hands['Player' + str(i)] = []
    #print(player_hands)

    random.shuffle(deck)

    # print(deck)

    for i in range(7):
        for j in range(1,len(player_hands) + 1):
            player_hands['Player' + str(j)].append(deck[0])
            del deck[0]
    
    # print(player_hands)
    # print(len(deck))
    
    count = 1
    
    discard.append(deck[0])
    deck.remove(deck[0])
    print(discard[0])

    while count <= (len(player_hands)):
        print('Player' + str(count) + "'s hand: ", player_hands['Player' + str(count)])
        index_of_card = ((int(input('Player %s, what number card would you like to play? ' % str(count)))) - 1)
        
        player_hand = player_hands['Player' + str(count)]
        card = player_hand[index_of_card]

        PlayCard(card, discard)

        if(CardIsNotMatch(discard, card)):
            DrawCard(deck, player_hand) # MAKE THEM DRAW HERE

        if len(player_hands['Player' + str(count)]) == 0:
            print('Player' + str(count) + ' wins!')
            count = 9
        count = count + 1
        if count == (len(player_hands) + 1):
           count = 1

def PlayCard(card, discard):
    if(CardIsMatch(discard, card)):
        discard.append(card)
        print('Discard Pile: ', discard[-1])
        del card
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
        discard[-1][1] != card[1] and CardIsNotWild(card)):
        return True
    return False

def CardIsMatch(discard, card):
    if(discard[-1][0] == card[0] or
        discard[-1][1] == card[1] or CardIsWild(card)):
        return True
    return False

def DrawCard(deck, player_hand):
    return player_hand.append(deck[0])

UNO()