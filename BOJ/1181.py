n = int(input())

l = [str(input()) for _ in range(n)]

l = list(set(l))

l.sort(key=lambda x : (len(x), x))

for i in l:
    print(i)