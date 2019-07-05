import math
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
z = abs(x) + abs(y)
zr = abs(xc) + abs(yc)
s = math.pi * r


def IsPointInCirle(x, y):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


if IsPointInCirle(x, y) is True:
    print('YES')
else:
    print('NO')
