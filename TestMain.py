# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

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
#Display main menu for the game and import correct file

# - Arguements: none.
# - Print main menu and allow player to choose option.
# - Ensure only game options are selectible.
# - Returns: nothing.

	print("Choose from the menu:")
	print("1 - Play a normal game (1 - 100)")
	print("2 - Play a modified game (1 - whatever)")
	print("3 - Let the computer run the game and see the results")
	print("4 - Quit")
	print()
	charFormat = str(input("Which do you want to do?... "))

	if charFormat == "1":
		print("New Game")
		import Classes as c
		Game = c.Game(100)
		Game.guessNumber()
		del Game
		mainMenu()

	elif charFormat == "2":
		print("New Modified Game")
		import Classes as c
		intMaximum = 0
		intMaximum = int(input("What do you want the maximum to be?... "))
		Game = c.Game(intMaximum)
		Game.guessNumber()
		del Game
		mainMenu()

	elif charFormat =="3":
		import Classes as c
		intMaximum = 0
		intRounds = 0
		intMaximum = int(input("What is the maximum for the simulations?... "))
		intRounds = int(input("How many simulations do you want to run?... "))
		Game = c.Game(intMaximum, intRounds)
		Game.guessNumber(intRounds)
		del Game
		mainMenu()

	elif charFormat == "4":
		print("Thanks for playing!")
		input()
		quit

	else:
		print("Please choose an option from the menu")
		print ()
		mainMenu()

mainMenu()

#========================

# def simGame(gameNum, maxGoal, currentGoal):
	# intMax = maxGoal
	# intMin = 0
	# intTry = 1
	# intGuess = 0
	
	# print ("Game ", gameNum, ", Game Range ", maxGoal, ", Goal Number ", currentGoal)
	
	# while intGuess != currentGoal:
		# intRange = int(intMax - intMin)
		# intGuess = int(intMin + (intRange / 2))
		# if intGuess < currentGoal:
			# print("Guess ", intTry, " -> ", intGuess, "too low")
			# intMin = intGuess
		# elif intGuess > currentGoal:
			# print("Guess ", intTry, " -> ", intGuess, "too high")
			# intMax = intGuess
		# else:
			# print("Guess ", intTry, " -> ", intGuess, " was correct")
		
		# intTry += 1
			

# def simRounds():
	# print("How many times do you want the computer to run this simulation?")
	
	# intLoops = 0
	# while intLoops < 1 or intLoops > 10:
		# try:
			# intLoops = int(input("Minimum 1, Maximum 10 ... "))
		# except:
			# print("You need to pick a number between 1 and 10")
			# input()
			# simRounds()
	# print()
	
	# return intLoops

# def playGame():
	# charAgain = "Y"
	# intHigh = 2
	# intRounds = 1
	# intGame = 0
	# import Game as G
	# import Modified as M
	
	# while charAgain == "Y":
		# charAgain = "Z"
		# import random as R
		# intMod = M.modGame()
		# intLoops = simRounds()
		# while intLoops > 0:
			# intLoops -= 1
			# intGame += 1
			# intRand = R.randrange(1, intMod)
			# simGame(intGame, intMod, intRand)
			# print()
			
		# intGame = 0
		# print("Would you like to run another simulation?")
		# charAgain = G.yOrN()

	
