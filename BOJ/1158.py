from collections import deque

n, m = map(int, input().split())

q = deque()

for i in range(n):
    q.append(i + 1)

print("<", end='')
while q:
    for _ in range(m - 1):
        q.append(q.popleft())
    print(q.popleft(), end='')
    if q:
        print(", ", end='')
print(">")
