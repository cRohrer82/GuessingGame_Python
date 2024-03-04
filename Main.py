# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

import math as M
from Messages import ErrorMessages as EM

print("WELCOME TO THE GUESSING GAME!\n\n"
"In this game a number is picked at random and then you try to guess\n"
"what that number is. After each guess you will be told if you are too\n"
"high or too low. After you find the number, you will get a message\n"
"on how many guesses you took. If you take too many, the message will\n"
"tell you how many you should have needed. Then you can try again to\n"
"improve your technique.\n"
"You can also let the computer run the game several times to see what\n"
"the maximum number of guesses should be and see what technique the\n"
"computer uses.")
print()

def mainMenu():
# Main menu
	print("Choose from the menu:")
	print("1 - Play a normal game (1 - 100)")
	print("2 - Play a modified game (1 - whatever)")
	print("3 - Let the computer run the game and see the results")
	print("4 - Quit")
	print()
	charFormat = str(input("Which do you want to do?... "))

# Option 1: Normal game (1-100)
	if charFormat == "1":
		print("New Game")
		
		import Classes.Game as G
		
		# Run game using 100 for max.
		Game = G.Game(100)
		Game.guessNumber()
		del Game
		print()
		
		# Return to main menu
		mainMenu()

# Option 2: Modified game (1-x)
	elif charFormat == "2":
		print("New Modified Game")
		
		import Classes.Game as G
		
		# Maximum for the game is limited to 2 billion. 'While' and 'Try' loop are for error catching.
		intMaximum = 0
		while M.isnan(intMaximum) or intMaximum < 2 or intMaximum > 2000000000:
			try:
				intMaximum = int(input("Pick a maximum for your game (must be between 2 and 2000000000)... "))
			except:
				continue
				
		# Run game using player input for max.
		Game = G.Game(intMaximum)
		Game.guessNumber()
		del Game
		print()
		
		# Return to main menu
		mainMenu()

# Option 3: Simulator (1-x, run by system)
	elif charFormat =="3":
		import Classes.Game as G
		
		# Maximum for the simulation is limited to 2 billion. 'While' and 'Try' loop are for error catching.
		intMaximum = 0
		intRounds = 0
		while M.isnan(intMaximum) or intMaximum < 2 or intMaximum > 2000000000:
			try:
				intMaximum = int(input("Pick a maximum for your simulation (must be between 2 and 2000000000)... "))
			except:
				continue
				
		# Minimum number of rounds is 1, maximum is 10. 'While' and 'Try' loop are for error catching.
		while M.isnan(intRounds) or intRounds < 1 or intRounds > 10:
			try:
				intRounds = int(input("How many simulations do you want to run? (must be between 1 and 10)... "))
			except:
				continue
					
		# 'For' loop runs simulation number of times entered by player. Simulation maximum is also entered by the player
		for x in range(intRounds):
			Game = G.Game(intMaximum)
			Game.s_guessNumber(x + 1)
			del Game
			print()
		print()
		
		# Return to main menu
		mainMenu()

# Option 4: Quit game
	elif charFormat == "4":
		print("Thanks for playing!")
		input()
		quit

# Invalid option
	else:
		print(EM.NotAnOptionError())
		print ()
		mainMenu()

# Start game
mainMenu()

#========================
