def rec(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return rec(a * a, n / 2)
    else:
        return a * rec(a, n - 1)


a = float(input())
n = int(input())
print(rec(a, n))
