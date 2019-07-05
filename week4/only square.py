import math


def sq():
    n = int(input())
    if n != 0:
        sq()
        if math.sqrt(n)**2 == n:
            global t
            t = 0
            print(n)


t = 1
sq()
if t:
    print(0)
