a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

k = 0
for x in range(1001):
    if x - e == 0:
        x += 1
        continue
    if x != e and ((a * x ** 3) + (b * x ** 2) + c * x + d) == 0:
        k += 1
print(k)
