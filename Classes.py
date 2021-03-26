# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

import random as R

#========================
class Player:
	'Represents the player'
	
	def __init__(self, name):
		self.name = name
		
	def makeGuess(self):
		'code'
		
	def makeGame(self):
		strGame = input("Enter a name for the game")
		intMax = int(input("What is the maximum for this game"))
		return Game(strGame, self.name, intMax)
		
		
#=========================
class Game:
	'Represents a game created by the player'
	
	intGoal = 0
	
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
		
		
#========================
class Guess:
	'Represents guesses made by the player'
	
	def __init__(self, player, number, game):
		self.player = player
		self.number = number
		self.game = game
		
	def makeGuess(self):
		'code'