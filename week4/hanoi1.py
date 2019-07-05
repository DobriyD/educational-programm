def hanoi_3(n, x, y):
    if n < 1:
        return
    if (x + 2) % 3 == y:
        hanoi_3(n - 1, x, y)
        print(x, "->", (x + 1) % 3)
        hanoi_3(n - 1, y, x)
        print((x + 1) % 3, "->", y)
        hanoi_3(n - 1, x, y)
    else:
        hanoi_3(n - 1, x, (x + 2) % 3)
        print(x, "->", y)
        hanoi_3(n - 1, (x + 2) % 3, y)


n = int(input())
hanoi_3(n, 1, 3)
