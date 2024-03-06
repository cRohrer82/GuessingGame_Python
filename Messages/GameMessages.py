# -*- coding: utf-8 -*-
"""
@author: Christopher Rohrer
"""

def InstructionMessage():
    return "Choose a number from 1 to {0}... "

def NotCorrectMessage():
    return "Nope, it's {0} than that"

def EndGameMessage(intGood, intGuesses):
    strMessage = "\nThat's it! Congratulations!\nIt took you {0} turns. ".format(intGuesses)
    if intGuesses <= intGood and intGuesses > 1:
        strMessage += "Good job!"
    elif intGuesses > intGood:
        strMessage += "Try to get it less than {0} turns next time".format(intGood)
    elif intGuesses == 1:
        strMessage += "Wow! That's great!"

    return strMessage

def SimGameData():
    return "Game {0}, Game Range {1}, Goal Number {2}"

def SimGameTurnData(boolCorrect):
    if not boolCorrect:
        return "Guess {0} -> {1} too {2}"
    else:
        return "Guess {0} -> {1} was correct"