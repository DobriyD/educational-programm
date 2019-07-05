string = input()
string = ''.join([string[i] for i in range(len(string)) if i % 3 != 0])
print(string)
