# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""
import Game as G

def modGame():
    intRant_M = -1
    #while intRant_M 
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
    intHigh = 2
    intRounds = 1
    while intHigh < randMax:
        intRounds += 1
        intHigh *= 2
        
    return intRounds

def playGame():
    charAgain = "Y"
    intRounds = 7
    
    while charAgain == "Y":
        charAgain = "Z"
        import random as R
        intMod = modGame()
        intRand = R.randrange(1, intMod)
        intRounds = modEnd(intMod)
        #print(intRand) #delete 1st # to debug
        intCount = G.gameLoop(intRand, -1, 0, intMod)
        print("Correct!  Good guess!")
        G.endGame(intCount, intRounds)
        print("Would you like to play again?")
        charAgain = G.yOrN()
