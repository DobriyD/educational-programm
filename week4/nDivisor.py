def MinDivisor(n, d=2):
    return d if n % d == 0 else MinDivisor(n, d + 1)


n = int(input())
print(MinDivisor(n))
