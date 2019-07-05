def xor(x, y):
    if x + y == 1:
        return True
    return False


x = int(input())
y = int(input())

if xor(x, y) is True:
    print(1)
else:
    print(0)
