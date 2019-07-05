x = float(input())
y = float(input())
z = abs(x) + abs(y)


def IsPointInSquare(x, y):
    return abs(z) <= 1


if IsPointInSquare(x, y) is True:
    print('YES')
else:
    print('NO')
