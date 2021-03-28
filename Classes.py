# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

import math as M
import random as R

#=========================
class Player:
	'code'

#=========================
class Game:
	'Represents a game created by the player'
	
	def __init__(self, name, max):
		self.name = name
		# self.player = player
		self.max = self.parseMax(max)
		self.goal = self.findGoal()
		self.turns = self.findGoodNumber()
		
	def findGoal(self):
		intGoal = R.randrange(1, self.max + 1)
		return intGoal
		
	def findGoodNumber(self):
		intHigh = 2
		intTurns = 1
		
		while intHigh <= self.max:
			intTurns += 1
			intHigh *= 2
			
		return intTurns
		
	def parseMax(self, max):
		while M.isnan(max) or max < 2 or max > 2000000000:
			max = int(input("Please choose a whole number that is greater than 1 and less than 2 billion!... "))
			
		return max
			
		
	def guessNumber(self):
		intGuesses = 0
		intGuess = int(input("Choose a number from 1 to ", self.max, "... "))
		while intGuess != self.goal:
			if M.isnan(intGuess) or intGuess < 1 or intGuess > self.max:
				print("Please guess whole numbers between 1 and the game maximum!\nPress 'Enter' to continue.")
				continue
				
			intGuesses += 1
			
			if intGuess > self.goal:
				print("Nope, it's less than that")
			if intGuess < self.goal:
				print("Nope, it's greater than that")
				
		return intGuesses
		
#=======================
	# intHigh = 2
	# intRounds = 1
	# while intHigh < randMax:
		# intRounds += 1
		# intHigh *= 2
		
	# return intRounds
