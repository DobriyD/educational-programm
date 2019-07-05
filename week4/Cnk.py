def f(n, k):
    if n == k or k == 0:
        return 1
    if n == 2 and k == 1:
        return 2
    if n == 2 and k == 2:
        return 1
    if n == 3 and k == 1:
        return 3
    if n == 3 and k == 2:
        return 3
    return f(n - 1, k - 1) + f(n - 1, k)


n = int(input())
k = int(input())

print(f(n, k))
