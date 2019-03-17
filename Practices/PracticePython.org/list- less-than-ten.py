# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_5 = []
for int in a:
    if int < 5:
        less_than_5.append(int)
for int in less_than_5: print(int)

for int in a:
    if int < 5:
        print(int)