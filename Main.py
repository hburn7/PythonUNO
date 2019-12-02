# NOTE: All classes must be above "Main" class.

import UnoCardModel

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
    
    uc = UnoCardModel.UnoCard('R', 6, '', '')
    print(uc.color, uc.number)