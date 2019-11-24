from Core.venv.Scripts.CodeFiles.Models import UnoCardModel

uc = UnoCardModel.UnoCard('R', 6, False)  # Instantiation of the 'UnoCardModel' class.
print(uc.color, uc.number, uc.special) # Returns "R 6 False"