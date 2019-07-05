x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1


if IsPointInSquare(x, y) is True:
    print('YES')
else:
    print('NO')
