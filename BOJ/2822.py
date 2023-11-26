
l = [[i + 1, int(input())] for i in range(8)]

l.sort(key=lambda x : x[1])
value = 0
arr = []

for i in range(len(l) - 1, 2, -1):
    arr.append(l[i][0])
    value += l[i][1]

arr.sort()

print(value)
for i in arr:
    print(i, end=' ')
