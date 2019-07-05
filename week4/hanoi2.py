def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish
        move(n - 1, start, temp)
        print(n, start, finish)
        move(n - 1, temp, finish)


start = 1
finish = 3
n = int(input())
move(n, start, finish)
