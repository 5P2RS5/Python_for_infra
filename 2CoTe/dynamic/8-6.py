import sys


n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

d = [0] * 100

d[0] = l[0]

d[1] = max(l[0], l[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + l[i])

print(d[n - 1])