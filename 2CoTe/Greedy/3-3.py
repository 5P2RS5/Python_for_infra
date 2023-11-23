
n, m = map(int, input().split())

a = 0
for i in range(0, n):
    temp = min(list(input().split(' ')))
    if a < int(temp):
        a = int(temp)

print(a)