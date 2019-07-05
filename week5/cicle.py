a = [int(i) for i in input().split()]


def shift(a, n):
    n = n % len(a)
    return a[n:] + a[:n]


print(*(shift(a, -1)), sep=' ')
