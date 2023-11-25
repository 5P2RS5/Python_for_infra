import sys

n, target = map(int, sys.stdin.readline().split())

coin = []

d = [10001] * (target + 1)
d[0] = 0

for i in range(n):
    coin.append(int(sys.stdin.readline()))


for i in range(n):
    for j in range(coin[i], target + 1):
        if (d[j - coin[i]]) != 10001:
            d[j] = min(d[j-coin[i]] + 1, d[j])

print(d)

if d[target] == 10001:
    print(-1)

else:
    print(d[target])



