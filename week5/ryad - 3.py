n = int(input())
if n == 1:
    mn = 1 ** (n - 1)
    mx = mn * 10 - 1
    print(*(x for x in range(mx, mn, -2)), 1)
elif n == 2:
    mn = 11
    mx = 99
    print(*(x for x in range(mx, mn, -2)), 11)
elif n == 3:
    mn = 111
    mx = 999
    print(*(x for x in range(mx, mn, -2)), 111)
elif n == 4:
    mn = 1111
    mx = 9999
    print(*(x for x in range(mx, mn, -2)), 1111)