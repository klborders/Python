
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import datetime

def when_will_i_be_100(name, age, copies):
    now = datetime.datetime.now()
    year = (now.year-age+100)
    message = f'Dear {name}, You will turn 100 in {year}'
    for i in range(copies):
        print(message + "\n")


name = input('What is your name? ')
age = int(input('What is your age? '))
copies = int(input('How many times should I repeat this? '))
when_will_i_be_100(name,age,copies)