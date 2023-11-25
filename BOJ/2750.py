import sys

n = int(sys.stdin.readline())

l = sorted([int(sys.stdin.readline()) for _ in range(n)])

for i in range(n):
    print(l[i])