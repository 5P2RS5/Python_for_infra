from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(y, x) : 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((y, x))

    while len(q) != 0 :
        py, px = q.popleft()

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[py][px] + 1
                q.append((ny, nx))
    return graph[n - 1][m - 1]    

print(bfs(0, 0))