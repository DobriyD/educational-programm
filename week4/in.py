a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    result = min(min1, min2)
    return result


print(min4(a, b, c, d))
