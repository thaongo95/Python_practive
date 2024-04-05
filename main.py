from frenchdeck import FrenchDeck
from random import choice

cards = FrenchDeck()

while(True):
	for i in range(3):
		print(choice(cards))
    # ~ q = input("Continue or not?")
    # ~ if q=='q':
		# ~ break
