import math
n = int(input())
m = int(input())


def ReduceFraction(n, m):
    k = math.gcd(n, m)
    return n // k, m // k


print(ReduceFraction(n, m)[0]), print(ReduceFraction(n, m)[1])
