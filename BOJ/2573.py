
#bfs

from collections import deque

def bfs(y, x, graph, visited, dy, dx, n, m):
    q = deque()
    q.append((y, x))
    
    visited[y][x] = True

    while q:
        py, px = q.popleft()

        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False and graph[ny][nx] > 0:
                visited[ny][nx] = True
                q.append((ny, nx))


if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = []
    
    for i in range(n):
        graph.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    answer = 0
    while True > 0:
        graph2 = [[int(0)] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0:
                    cnt = 0
                    for k in range(4):
                        if graph[i + dy[k]][j + dx[k]] <= 0 :
                            cnt += 1
                        graph2[i][j] = graph[i][j] - cnt
        
        visited = [[False] * m for _ in range(n)]
        result = 0
        for i in range(n):
            for j in range(m):
                if graph2[i][j] > 0 and visited[i][j] != True:
                    bfs(i, j, graph2, visited, dy, dx, n, m)
                    result += 1

        if result == 0 or result > 1:
            if result == 0:
                print(0)
            else:
                print(answer + 1)
            break
        graph = [i[:] for i in graph2]
        answer += 1