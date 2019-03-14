# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

'''
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / 
odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.

Ask the user for two numbers: one number to check (call it num) and one number to 
divide by (check). If check divides evenly into num, tell that to the user. If not, 
print a different appropriate message.
'''

def odd_or_even(int, check):
    if check == 0:
        return 'Your check can''t be zero'
    elif int % check == 0:
        return f"{int} is divisble by {check}"
    elif int % 4 == 0:
        return 'multiple of 4'
    elif int % 2 == 0:
        return 'even'
    else:
        return  'odd'

number = int(input('Give me a number: '))
check = int(input('Check to se if number is divisble by... '))
print(odd_or_even(number,check))

        