from Core.venv.Scripts.CodeFiles.Models import UnoCardModel

print('Welcome to Harry, Jordan, and Frankie\'s Python UNO!')

# We use while True because if someone puts in a wrong input they will now be re-prompted.
# while True:
#     try:
#         numPlayers = int(input('How many players will be playing? Please enter a value between 2 and 8: '))
#         if 2 <= numPlayers <= 8:
#             break
#         print('Invalid number, please try again.')
#     except ValueError:
#         print("You have entered an invalid input. Please try again.")

# ** I COMMENTED THE ABOVE SO THAT WE DON'T HAVE TO TYPE IT IN EVERY TIME WE WANNA DEBUG! :D **

uc = UnoCardModel.UnoCard('R', 6, '')  # Instantiation of the 'UnoCardModel' class.
print(uc.color, uc.number, uc.special)  # Returns "R 6 False"

special = UnoCardModel.OtherSpecial('D4')  # Draw 4.

print(special.type)
