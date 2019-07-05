import math


def IsPointInArea(x, y):
    st01 = math.sqrt((x - 1) ** 2 + (y - 1) ** 2) <= 2
    st02 = math.sqrt((x - 1) ** 2 + (y - 1) ** 2) >= 2
    st1 = y >= -x and y >= 2*x + 2 and st01
    st2 = y <= -x and y <= 2*x + 2 and st02
    return st1 or st2


x = float(input())
y = float(input())

if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')
