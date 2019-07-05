def hanoi(n, x, y):
    if n > 0:
        if x % 3 + 2 == 0:
            hanoi(n - 1, x, y)
            print(n, x, x % 3 + 1)
            hanoi(n - 1, y, x)
            print(n, x % 3 + 1, y)
            hanoi(n - 1, x, y)
        else:
            hanoi(n - 1, x, 6 - x - y)
            print(n, x, x % 3 + 1)
            hanoi(n - 1, 6 - x - y, y)


n = int(input())
x = 1
y = 3

hanoi(n, x, y)
