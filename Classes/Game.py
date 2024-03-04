# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

import math as M
import random as R
from Messages import ErrorMessages as EM
from Messages import GameMessages as GM

###################
# Represents a game
###################
class Game:

	################################
	# Creates instance of Game class
	################################
	def __init__(self, max):
		# self.name = name
		# self.player = player
		self.max = max
		self.goal = self.__findGoal()
		self.goodNumberOfTurns = self.__findGoodNumberOfTurns()
		
	#############################################################
	# *PRIVATE* Uses Random library to create a goal for the game
	#############################################################
	def __findGoal(self):
		intGoal = R.randrange(1, self.max + 1)
		#print(intGoal) #Comment line out BEFORE publishing. For debug use ONLY!
		
		return intGoal
		
	############################################################################
	# *PRIVATE* Returns a "good" number of trys, depending on the game's maximum
	############################################################################
	def __findGoodNumberOfTurns(self):
		intHigh = 2
		intTurns = 1
		
		while intHigh <= self.max:
			intTurns += 1
			intHigh *= 2
			
		return intTurns
				
	#####################################################################
	# Runs game. Checks guesses for validity and prints clues to the goal
	#####################################################################
	def guessNumber(self):
		intGuesses = 0
		intGuess = 0
		turnMessage = GM.InstructionMessage()

		while intGuess != self.goal:
			try:
				intGuess = int(input(turnMessage.format(self.max)))
			except:
				turnMessage = EM.RangeError()
				continue
				
			if M.isnan(intGuess) or intGuess < 1 or intGuess > self.max:
				print(EM.RangeError().format(self.max))
				input()
				continue
				
			intGuesses += 1
			
			if intGuess > self.goal:
				print(GM.NotCorrectMessage().format("less"))
			if intGuess < self.goal:
				print(GM.NotCorrectMessage().format("more"))
				
		self.endGame(intGuesses)
		
	#############################################
	# Ends game and lets player know how they did
	#############################################
	def endGame(self, intGuesses):
		print(GM.EndGameMessage(self.goodNumberOfTurns, intGuesses))
			
	#################################################################################
	# Formats simulations into readable data and uses a simple engine to make guesses
	#################################################################################
	def s_guessNumber(self, intGameNbr):
		intMax = self.max
		intMin = 0
		intTry = 1
		intGuess = 0
		intPreviousGuess = -1
		
		print (GM.SimGameData().format(intGameNbr, self.max, self.goal))
		
		while intGuess != self.goal:
			intRange = int(intMax - intMin)
			intGuess = int(intMin + (intRange / 2))

			if intGuess == intPreviousGuess:
				intGuess += 1

			intPreviousGuess = intGuess

			if intGuess < self.goal:
				print(GM.SimGameTurnData(False).format(intTry, intGuess, "low"))
				intMin = intGuess
			elif intGuess > self.goal:
				print(GM.SimGameTurnData(False).format(intTry, intGuess, "high"))
				intMax = intGuess
			else:
				print(GM.SimGameTurnData(True).format(intTry, intGuess))
			
			intTry += 1			
