n = int(input())
if n > 0:
    mn = int('1' * n)
    mx = int('9' * n)
    print(*(x for x in range(mx, mn, -2)), mn)
else:
    print(0)
