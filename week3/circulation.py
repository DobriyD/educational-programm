import math

n = float(input())
i = math.floor(n)
m = n - i

if m >= 0.5:
    print(math.ceil(n))
else:
    print(i)
