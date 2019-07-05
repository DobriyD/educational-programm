n = 4
for i in range(n):
    data = [int(s) for s in input().split()]
val = list(map(int, data.split()))
res = ['I' for x in range(val[0])]
for l, r in list(zip(val[2::2], val[3::2])):
    res[l-1: r] = len(res[l-1: r]) * ['.']
print(res)
