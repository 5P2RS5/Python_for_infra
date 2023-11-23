i = int(input())

l = []
for i in range(0, i):
    l.append(int(input()))

l.sort(reverse = True)

for i in l:
    print(i, end=' ')