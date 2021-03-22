# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

import Game as G
import Modified as M

def simGame(gameNum, maxGoal, currentGoal):
    intMax = maxGoal
    intMin = 0
    intTry = 1
    intGuess = 0
    
    print ("Game ", gameNum, ", Game Range ", maxGoal, ", Goal Number ", currentGoal)
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
    charAgain = "Y"
    intHigh = 2
    intRounds = 1
    intGame = 0
    
    while charAgain == "Y":
        charAgain = "Z"
        import random as R
        intMod = M.modGame()
        intLoops = simRounds()
        while intHigh < intMod:
            intRounds += 1
            intHigh *= 2
        while intLoops > 0:
            intLoops -= 1
            intGame += 1
            intRand = R.randrange(1, intMod)
            simGame(intGame, intMod, intRand)
            print()
            
        #intCount = G.gameLoop(intRand, -1, 0, intMod)
        #G.endGame(intCount, intRounds)
        print("Would you like to run another simulation?")
        charAgain = G.yOrN()
