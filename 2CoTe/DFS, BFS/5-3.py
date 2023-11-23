dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())

visited=[[False]*m for _ in range(n)]
l = []
answer = 0

def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if(ny >= n or nx >= m or nx < 0 or ny < 0):
            continue
        if l[ny][nx] == 1 or visited[ny][nx] == True:
            continue
        dfs(ny, nx)

for i in range(n):
    temp = input()
    l.append([])
    for j in range(m):
        l[i].append(int(temp[j]))

for i in range(0, n):
    for j in range(0, m):
        if l[i][j] == 0 and visited[i][j] == False : 
            dfs(i, j)
            answer += 1

print(answer)