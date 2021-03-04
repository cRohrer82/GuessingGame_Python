# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 2019
Modified on Tue Jun 30 2020

@author: Christopher Rohrer

"""

print("WELCOME TO THE GUESSING GAME!")
print("In this game a number is picked at random and then you try to guess")
print("what that number is. After each guess you will be told if you are too")
print("high or too low. After you find the number, you will get a message")
print("on how many guesses you took. If you take too many, the message will")
print("tell you how many you should have needed. Then you can try again to")
print("improve your technique.")
print("You can also let the computer run the game several times to see what")
print("the maximum number of guesses should be and see what technique the")
print("computer uses.")
print()

def mainMenu():
    print("Choose from the menu:")
    print("1 - Play a normal game (1 - 100)")
    print("2 - Play a modified game (1 - whatever)")
    print("3 - Let the computer run the game and see the results")
    print("4 - Quit")
    print()
    charFormat = str(input("Which do you want to do?... "))

    if charFormat == "1":
        print("New Game")
        import Game as G
        G.playGame()
        mainMenu()

    elif charFormat == "2":
        print("New Modified Game")
        import Modified as M
        M.playGame()
        mainMenu()

    elif charFormat =="3":
        import Simulator as S
        S.playGame()
        mainMenu()

    elif charFormat == "4":
        print("Thanks for playing!")
        input()
        quit

    else:
        print("Please choose an option from the menu")
        print ()
        mainMenu()

mainMenu()
    
