# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
def is_palindrome(str):
    if str == str[::-1]:
        return f'{str} is a palindrome.'
    else:
        return f'{str} is not a palindrome.'

str = input('Input a word to check whether or not it is a palindrome: ')
print(is_palindrome(str))