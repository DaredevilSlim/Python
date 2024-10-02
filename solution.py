a = ''
b = 0
for i in sorted(map(str, input())):
    a += i
print(a.replace('0'), a[::-1])
