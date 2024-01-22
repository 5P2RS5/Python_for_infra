# bfs
from collections import deque

def bfs(graph, visited, n, m, y, x):
    visited[y][x] = True
    q = deque()
    q.append((y, x))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    wolf = 0
    sheep = 0

    while q:
        py, px = q.popleft()
        if graph[py][px] == 'v':
                wolf += 1
        if graph[py][px] == 'o':
                sheep += 1
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == False and graph[ny][nx] != '#':
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    
    
    if wolf >= sheep:
        return wolf, 0
    else :
        return 0, sheep







if __name__ == "__main__":
    n, m = map(int, input().split())
    sheep = 0
    wolf = 0
    graph = []
    for i in range(n):
        graph.append(list(map(str,input())))

    visited = [[False] * m for _ in range(n)] 

    for i in range(n):
        for j in range(m):
            if graph[i][j] != '#' and visited[i][j] == False:
                w, s = bfs(graph, visited, n, m, i, j)
                sheep += s
                wolf += w
    
    print(sheep, wolf)
    
