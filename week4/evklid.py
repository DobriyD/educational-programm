def NOD(a, b):
    if b == 0:
        return a
    else:
        return NOD(b, a % b)


a = int(input())
b = int(input())
print(NOD(a, b))
