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
		mainMenu()

	elif charFormat == "2":
		print("New Modified Game")
		import Modified as M
		M.playGame()
		mainMenu()

	elif charFormat =="3":
		import Simulator as S
		S.playGame()
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
	
