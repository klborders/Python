# daily challenges done on https://edabit.com
# Difficulty: Very Easy

# How Edabit Works
def hello():
    return "hello edabit.com"

# Return the Sum of Two Numbers
def addition(a, b):
    return a+b

# Return the Next Number from the Integer Passed
def addition(num):
	return num+1

# Profitable Gamble
def profitable_gamble(prob, prize, pay):
	return prob*prize-pay > 0

# Is the Word Singular or Plural?
def is_plural(word):
	return word[-1]=='s'

# Concatenate First and Last Name into One String
def concat_name(first_name, last_name):
	return '%s, %s'%(last_name,first_name)

# Is the Number Less than or Equal to Zero?
def lessThanOrEqualToZero(num):
	return num<=0

# To the Power of _____
def calculate_exponent(num, exp):
    return num**exp
    
# Find the Largest Number in a List
def findLargestNum(nums):
	return max(nums)

# Find the Smallest Number in a List
def findSmallestNum(lst):
    return min(lst)

# Compare Strings by Sum of Characters
def comp(txt1, txt2):
	return len(txt1) == len(txt2)

# Return the Last Element in a List
def getLastItem(lst):
	return lst[-1]	

# Multiple of 100
def divisible(num):
	return num % 100 == 0

# Count Syllables
def number_syllables(word):
	return len(word.split('-'))

# Slice of Pie
def equal_slices(total, people, each):
	return people * each <= total