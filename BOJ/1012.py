import sys
sys.setrecursionlimit(10**5)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= n or nx >= m or ny < 0 or nx < 0:
            continue
        if arr[ny][nx] == 0 or visited[ny][nx]:
            continue
        dfs(ny, nx)


T = int(input())

for _ in range(T):
    n, m, k = map(int, input().split())
    answer = 0
    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and (not visited[i][j]) :
                dfs(i, j)
                answer += 1
    print(answer)



    

