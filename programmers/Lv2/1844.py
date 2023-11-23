from collections import deque

def solution(maps):
    answer = 0
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    q = deque()
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    cost = [[0] * m for _ in range(n)]
    q.append([0, 0])
    visited[0][0] = True
    
    while len(q) != 0:
        temp = q.popleft()
        py = temp[0]
        px = temp[1]
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            if(ny >= n or nx >= m or ny < 0 or nx < 0):
                continue
            if(visited[ny][nx] or maps[ny][nx] == 0):
                continue
            q.append([ny, nx])
            cost[ny][nx] = cost[py][px] + 1
            visited[ny][nx] = True
    
    
    if(cost[n-1][m-1] == 0):
        return -1
    
    return cost[n - 1][m - 1] + 1