n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

l = sorted(l, key=lambda x : (x[1], x[0]))

for i in l:
    print(i[0], i[1])