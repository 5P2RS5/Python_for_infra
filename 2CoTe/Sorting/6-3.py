from collections import defaultdict

cnt = int(input())

dic = defaultdict()

for i in range(0, cnt):
    n, m = map(str, input().split())
    dic[n] = int(m)

print(dic)

dic = sorted(dic.items(), key = lambda x : x[1])

for i in dic:
    print(i[0], end=' ')