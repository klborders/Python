# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

n = int(input('Find the divisor of: '))
for int in range(1,n):
    if n % int == 0:
        print(int)