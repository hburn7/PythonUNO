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

    while count <= (len(player_hands)):
        print('Player' + str(count) + "'s hand: ", player_hands['Player' + str(count)])
        index_of_card = ((int(input('Player %s, what number card would you like to play? ' % str(count)))) - 1)

        card = player_hands['Player' + str(count)][index_of_card]

        if(discard[-1][0] != card[0] and
          discard[-1][1] != card[1] and CardIsNotWild(card)):
            continue # MAKE THEM DRAW HERE

        discard.append(card)
        print('Discard Pile: ', discard[-1])
        del card
        #print(player_hands['Player' + str(count)])
        if len(player_hands['Player' + str(count)]) == 0:
            print('Player' + str(count) + ' wins!')
            count = 9
        count = count + 1
        if count == (len(player_hands) + 1):
            count = 1

def CardIsNotWild(card):
    if(card[0] != 'W'):
        return True
    return False

UNO()