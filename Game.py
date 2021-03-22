# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer

charAgain -> Repeat the game if player wants.
charMod   -> Tell the program if the player wants to use a different range than
             the default 100.
intRounds -> Max number of rounds player should take.
intMod    -> Modified maximum for the game.
intRand   -> Hold the goal number for the game.
intCount  -> Hold the number of tries the player had.

gameLoop:
    randGoal    -> Goal for the game.
    playerInput -> Player's guess for this round.
    loopCount   -> Number of rounds the player has used.
    maxGoal     -> Maximum for the game.
    
endGame:
    loopCount -> Number of rounds the player has used.
    goodCount -> Number of rounds for a good game.
    
yOrN:
    charResp -> Player's choice of yes (y) or no (n).
"""

def gameLoop(randGoal, playerInput, loopCount, maxGoal):
"""
Guessing loop for player guesses

- Arguements: goal for the game, initialize player input, initialize loop count, maximum possible goal for game.
- Ensures good values for the game are entered.
- Lets player know if guess is too high or too low.
- Returns: number of player guesses.
"""
    while playerInput != randGoal:
        try:
            print("Pick a number from 1 to", maxGoal,"... ")
            playerInput = int(input())
        except ValueError:
            print("Your response must be a whole number!")
            print("Please try again...")
            continue 
        if playerInput > maxGoal:
            print("Your game max is ", maxGoal)
            continue
        if playerInput < 1:
            print("Game minimum is always 1")
            continue
        loopCount += 1
        if playerInput < randGoal:
            print("Nope, it's greater than that")
        if playerInput > randGoal:
            print("Nope, it's less than that")
    return loopCount

def endGame(loopCount, goodCount):
"""
Response after guessing correct number

- Arguements: number of guesses, maximum number of guesses for good game.
- Takes loop count and compares to number of guesses for good game.
- Returns: nothing.
"""
    if loopCount > 1 and loopCount <= goodCount:
        print("It took you", loopCount, "guesses.")
    elif loopCount == 1:
        print("It took you", loopCount, "guess!  Wow you're good at this!!")
    elif loopCount >= goodCount:
        print("It took you", loopCount, "guesses.")
        print("Hmm... it really shouldn't take you more than", str(goodCount))
    print()

def yOrN():
"""
Loop for deciding to play another game or not

- Arguements: none.
- Makes sure player can only continue if n or y is selected.
- Returns: N for no or Y for yes.
"""
    charResp = ""
    while charResp != "N" and charResp != "Y":
        charResp = str(input("Push 'n' then 'enter' for no, push 'y' then 'enter' for yes,"))
        charResp = charResp.upper()
        print()
    return charResp

def playGame():
"""
Sets up game and loops if players wants to play more than once

- Arguements: none.
- Imports 'random' library and uses it to create random number for game goal.
- Lets player know when they guessed correctly and calls end game with game data.
- Asks player if they want to play the game again and loops around to begining if they do.
- Returns: nothing.
"""
    charAgain = "Y"
	
    while charAgain == "Y":
        charAgain = "Z"
        import random as R
        intRand = R.randrange(1,101) #-> 
        #print(intRand) #delete 1st # to debug
        intCount = gameLoop(intRand, -1, 0, 100)
        print("Correct!  Good guess!")
        endGame(intCount, 7)
        print("Would you like to play again?")
        charAgain = yOrN()
	
