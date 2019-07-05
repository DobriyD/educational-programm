def IsAscending(A):
    i = 0
    try:
        while A[i] < A[i+1]:
            i += 1
        return "NO"
    except IndexError:
        return "YES"


A = input().split()
print(IsAscending(A))
