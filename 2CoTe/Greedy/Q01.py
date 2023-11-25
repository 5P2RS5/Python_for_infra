import sys
from collections import defaultdict

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

d = [0] * (n)

for i in range(0, n):
    print(l[i])
    d[l[i]] += 1

h = max(l)

print(d)
result = 0
for i in range(h, 0, -1):
    if(d[i] >= i):
        print(d[i], i)
        result += 1

print("result", result)


