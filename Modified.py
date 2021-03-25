# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

def modGame():
# Set maximum for the modified game

# - Arguements: none.
# - Prompt player for game maximum.
# - Ensure maximum value is a positive whole number.
# - Returns: maximum for modified game.

	intRant_M = -1

	try:
		intRant_M = int(input("What is the max for your game?... "))
		
	except ValueError:
		print("Your response must be a whole number!")
		print("Please try again...")
		print(intRant_M)
		modGame()
	if intRant_M < 1:
		print("Please pick a whole number greater than 0")
		modGame()
		
	return intRant_M

def modEnd(randMax):
# Define good number of turns

# - Arguements: modified game maximum.
# - Calculate good number of guesses.
# - Returns: good number of guesses.

	intHigh = 2
	intRounds = 1
	while intHigh < randMax:
		intRounds += 1
		intHigh *= 2
		
	return intRounds

def playGame():
# Run modified game

# - Arguements: none.
# - Create loop so player can play multiple games.
# - Set maximum value, goal number, and good number of guesses.
# - Call gameLoop to run modified game and show when player gets correct guess.
# - Ask to play again and call yOrN.
# - Returns: nothing.

	charAgain = "Y"
	intRounds = 7
	
	while charAgain == "Y":
		import random as R
		import Game as G
		
		charAgain = "Z"
		
		intMod = modGame()
		intRand = R.randrange(1, intMod)
		intRounds = modEnd(intMod)
		
		#print(intRand) #delete 1st # to debug
		intCount = G.gameLoop(intRand, -1, 0, intMod)
		print("Correct!  Good guess!")
		G.endGame(intCount, intRounds)
		
		print("Would you like to play again?")
		charAgain = G.yOrN()
