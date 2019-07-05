import math
n = int(input())


def IsPrime(n):
    i = 2
    limit = int(math.sqrt(n))
    while i <= limit:
        if n % i == 0:
            print('NO')
            quit()
        i += 1

    print('YES')


IsPrime(n)
