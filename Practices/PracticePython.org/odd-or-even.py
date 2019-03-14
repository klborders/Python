# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

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

        
