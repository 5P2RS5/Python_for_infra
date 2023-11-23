a, b = map(int, input().split())

n = list(map(int, input().split()))
m = list(map(int, input().split()))

n.sort()
m.sort(reverse=True)



for i in range(b):
    n[i], m[i] = m[i], n[i]

print(sum(n))