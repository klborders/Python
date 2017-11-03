# This Python file uses the following encoding: utf-8
# Python sprint for November 11 2017
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
#
# Dice Rolling Simulator
#
# The Goal: Like the title suggests, this project involves writing a program
# that simulates rolling dice. When the program runs, it will randomly choose a
# number between 1 and 6. (Or whatever other integer you prefer — the number of
# sides on the die is up to you.) The program will print what that number is.
# It should then ask you if you’d like to roll again. For this project, you’ll
# need to set the min and max number that your dice can produce. For the
# average die, that means a minimum of 1 and a maximum of 6. You’ll also want a
# function that randomly grabs a number within that range and prints it.
# Concepts to keep in mind:
#
# Random
# Integer
# Print
# While Loops
#
# A good project for beginners, this project will help establish a solid
# foundation for basic concepts. And if you already have programming
# experience, chances are that the concepts used in this project aren’t
# completely foreign to you. Print, for example, is similar to Javascript’s
# console.log.

from random import randint

def roll_dice():
    x = input('How many sides are on the dice? ')
    if isinstance(int(x), int):
        return randint(1, int(x))
    else:
        print('Invalid input! Ensure input is an integer.')
        return exit()

def rolling():
    user_input = 'y'
    while user_input.lower() == 'y':
        print(roll_dice())
        user_input = raw_input("Would you like to roll again?(Y/n) ")

rolling()
