import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def distance(x1, y1, x2, y2):
    dist = math.hypot(x2 - x1, y2 - y1)
    return dist


print(distance(x1, y1, x2, y2))
