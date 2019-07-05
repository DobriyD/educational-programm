def sumNCubes(n):
    return sum(i**3 for i in range(1,n+1))

n = int(input())
print(sumNCubes(n))
