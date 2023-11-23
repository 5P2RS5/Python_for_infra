from collections import deque

n, m = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

l = []
visited = [[False] * m for _ in range(n)]
cost = [[0] * m for _ in range(n)]

for i in range(n):
    l.append([])
    temp = input()
    for j in range(m):
        l[i].append(temp[j])

y, x = 0, 0

def bfs(y, x):
    visited[y][x] = True
    q = deque()
    q.append([y, x])
    while len(q) != 0:
        p = q.popleft()

        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]

            if(ny >= n or nx >= m or nx < 0 or ny < 0):
                continue
            if(visited[ny][nx] == True or l[ny][nx] == 0):
                continue
            q.append([ny, nx])
            visited[ny][nx] = True
            cost[ny][nx] = cost[p[0]][p[1]] + 1
    print(cost[n - 1][m - 1] + 1)


bfs(0, 0)
print(cost)        
    