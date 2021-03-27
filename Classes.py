# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

import random as R

#=========================
class Player:
	'code'

#=========================
class Game:
	'Represents a game created by the player'
	
	intGuesses = 0
	
	def __init__(self, name, player, max):
		self.name = name
		self.player = player
		self.max = max
		self.goal = findGoal()
		
	def makeMessage(self):
		'code'
		
	def findGoodNumber(self, max):
		'code'
		
	def findGoal(self):
		intGoal = R.randrange(1, self.max + 1)
		return intGoal
		
	def guessNumber(self, number):
		intGuesses += 1
		return 
		
#=======================
