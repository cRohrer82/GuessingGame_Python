# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""


def simGame(gameNum, maxGoal, currentGoal):
# Display for simulated games

# - Arguements: current simulation number, maximum goal for simulations, current simulation goal.
# - Runs a single simulation of a game.
# - Each simulation gets a title and each guess gets a note
# - Returns: nothing.

	intMax = maxGoal
	intMin = 0
	intTry = 1
	intGuess = 0
	
	# Simulation Title:
	print ("Game ", gameNum, ", Game Range ", maxGoal, ", Goal Number ", currentGoal)
	
	# Simulation Guess Note:
	while intGuess != currentGoal:
		intRange = int(intMax - intMin)
		intGuess = int(intMin + (intRange / 2))
		if intGuess < currentGoal:
			print("Guess ", intTry, " -> ", intGuess, "too low")
			intMin = intGuess
		elif intGuess > currentGoal:
			print("Guess ", intTry, " -> ", intGuess, "too high")
			intMax = intGuess
		else:
			print("Guess ", intTry, " -> ", intGuess, " was correct")
		
		intTry += 1
			

def simRounds():
# Define the number of times to run the simulation

# - Arguements: none.
# - Prompt player to enter number of simulation runs.
# - Only allow between 1 and 10 simulations.
# - Returns: number of simulations to run.

	print("How many times do you want the computer to run this simulation?")
	
	intLoops = 0
	while intLoops < 1 or intLoops > 10:
		try:
			intLoops = int(input("Minimum 1, Maximum 10 ... "))
		except:
			print("You need to pick a number between 1 and 10")
			input()
			simRounds()
	print()
	
	return intLoops

def playGame():
# Define parameters for the simulation(s)

# - Arguements: none.
# - Create and ready variables and import needed files.
# - Define parameters and run simulation(s).
# - Ask if player would like to run more simulations.
# - Returns: nothing.

	charAgain = "Y"
	intHigh = 2
	intRounds = 1
	intGame = 0
	import Game as G
	import Modified as M
	
	while charAgain == "Y":
		charAgain = "Z"
		import random as R
		intMod = M.modGame()
		intLoops = simRounds()
		while intLoops > 0:
			intLoops -= 1
			intGame += 1
			intRand = R.randrange(1, intMod)
			simGame(intGame, intMod, intRand)
			print()
			
		print("Would you like to run another simulation?")
		charAgain = G.yOrN()
