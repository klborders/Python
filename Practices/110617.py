# This Python file uses the following encoding: utf-8
# Python sprint for November 11 2017
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
#
# Guess the number
#
# The Goal: Similar to the first project, this project also uses the random
# module in Python. The program will first randomly generate a number unknown
# to the user. The user needs to guess what that number is. (In other words,
# the user needs to be able to input information.) If the user’s guess is
# wrong, the program should return some sort of indication as to how wrong
# (e.g. The number is too high or too low). If the user guesses correctly, a
# positive indication should appear. You’ll need functions to check if the user
# input is an actual number, to see the difference between the inputted number
# and the randomly generated numbers, and to then compare the numbers.
# Concepts to keep in mind:
#
# Random function
# Variables
# Integers
# Input/Output
# Print
# While loops
# If/Else statements
#
# Jumping off the first project, this project continues to build up the base
# knowledge and introduces user-inputted data at its very simplest. With user
# input, we start to get into a little bit of variability.
from random import randint

num = randint(1,100)

def get_guess():
    guess = int(input('Guess the number: '))
    validate_guess(guess)

def validate_guess(g):
    if isinstance(g, int):
        get_result(g)
    else:
        'Invalid input, guess again.'
        get_guess()

def get_result(g):
    if num == g:
        print 'You are correct!'
    elif num > g:
        print 'Higher... Try again.'
        get_guess()
    elif num < g:
        print 'Lower... Try again.'
        get_guess()

get_guess()
