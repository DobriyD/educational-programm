a = [int(i) for i in input().split()]

index = input()

b = index.split()

k = int(b[0])

c = int(b[1])

a.append('')

for i in range(len(a) - 1, k, -1):

    a[i] = a[i-1]

a[k] = str(c)

print(' '.join(str(i) for i in a))
