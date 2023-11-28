from collections import deque

n, m, k = map(int, input().split())

q = deque()

for i in range(n):
    q.append(i + 1)



isleft = False
cnt = 0
while q:
    if not isleft :
        for i in range(m - 1):
            q.append(q.popleft())
        print(q.popleft())
    else :
        for i in range(m - 1):
            q.appendleft(q.pop())
        print(q.pop())
    cnt += 1
    if cnt % k == 0 : 
        isleft = not isleft
