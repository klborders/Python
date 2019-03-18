# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
import random

def compare_list(list_a, list_b):
    return [set(list_a) & set(list_b)]

def generate_random_number_list():
    random_number_list = []
    amount = random.randint(3,20)
    for i in range (amount):
        random_number_list.append(random.randrange(1,20,1))
    return random_number_list

a = generate_random_number_list()
b = generate_random_number_list()
print((compare_list(a, b)))