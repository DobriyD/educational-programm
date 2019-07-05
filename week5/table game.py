n = int(input())
k = 0
for i in range(1, n + 1):
    k += i
for i in range(n - 1):
    k -= int(input())
print(k)
