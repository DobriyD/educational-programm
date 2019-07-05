def power(a, n):
    if a == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return a
    elif n < 0:
        while n < 0:
            a = 1 / (a * (a ** (- n - 1)))
            n += 1
    else:
        while n > 0:
            a = a * a ** (n - 1)
    print(a)


a = float(input())
n = int(input())
power(a, n)
