# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

import math as M
import random as R

#=========================
# class Player:
	# Represents a player
	
	# code

#=========================
class Game:
	# Represents a game
	
	def __init__(self, max):
		# self.name = name
		# self.player = player
		self.max = self.parseMax(max)
		self.goal = self.findGoal()
		self.turns = self.findGoodNumber()
		
	def parseMax(self, max):
		while M.isnan(max) or max < 2 or max > 2000000000:
			max = int(input("Please choose a whole number that is greater than 1 and less than 2 billion!... "))
			
		return max
		
	def parseRounds(self, rounds):
		while M.isnan(rounds) or rounds < 1 or rounds > 10:
			rounds = int(input("Please enter a number from 1 to 10... "))
			
		return rounds
			
	def findGoal(self):
		intGoal = R.randrange(1, self.max + 1)
		#print(intGoal) #Comment line out BEFORE publishing. For debug use ONLY!
		
		return intGoal
		
	def findGoodNumber(self):
		intHigh = 2
		intTurns = 1
		
		while intHigh <= self.max:
			intTurns += 1
			intHigh *= 2
			
		return intTurns
				
	def guessNumber(self):
		intGuesses = 0
		intGuess = 0
		while intGuess != self.goal:
			try:
				intGuess = int(input("Choose a number from 1 to game max... "))
			except:
				continue
				
			if M.isnan(intGuess) or intGuess < 1 or intGuess > self.max:
				print("Please guess whole numbers between 1 and the game maximum of ", self.max, "!\nPress 'Enter' to continue.")
				input()
				continue
				
			intGuesses += 1
			
			if intGuess > self.goal:
				print("Nope, it's less than that")
			if intGuess < self.goal:
				print("Nope, it's greater than that")
				
		self.endGame(intGuesses)
		
	def endGame(self, guesses):
		print("That's it! Congratulations!\nIt took you ", guesses, " turns.")
		if guesses <= self.turns and guesses > 1:
			print("Good job!")
		if guesses > self.turns:
			print("Try to get it less than ", guesses, " turns next time")
		if guesses == 1:
			print("Wow! That's great!")
			print()
			
	def s_guessNumber(self, gameNum):
		intMax = self.max
		intMin = 0
		intTry = 1
		intGuess = 0
		
		print ("Game ", gameNum, ", Game Range ", self.max, ", Goal Number ", self.goal)
		
		while intGuess != self.goal:
			intRange = int(intMax - intMin)
			intGuess = int(intMin + (intRange / 2))
			if intGuess < self.goal:
				print("Guess ", intTry, " -> ", intGuess, "too low")
				intMin = intGuess
			elif intGuess > self.goal:
				print("Guess ", intTry, " -> ", intGuess, "too high")
				intMax = intGuess
			else:
				print("Guess ", intTry, " -> ", intGuess, " was correct")
			
			intTry += 1
			
#========================