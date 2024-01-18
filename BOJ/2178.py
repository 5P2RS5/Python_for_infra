# bfs

from collections import deque

def bfs(visited, graph, n, m):
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        py, px = q.popleft()
        
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m :
                continue
            if visited[ny][nx] == True or graph[ny][nx] == 0:
                continue
            q.append((ny, nx))
            graph[ny][nx] = graph[py][px] + 1
            visited[ny][nx] = True
    
    print(graph[n - 1][m - 1])
        







if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    
    visited = [[False] * m for _ in range(n)]
    bfs(visited, graph, n, m)