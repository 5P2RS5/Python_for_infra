# bfs

from collections import deque

def bfs(graph, visited, y, x, n):
    q = deque()
    result = 1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    q.append((y, x))
    visited[y][x] = True

    while q :
        py, px = q.popleft()
        
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            if ny >= n or nx >= n or ny < 0 or nx < 0:
                continue
            if visited[ny][nx] == True or graph[ny][nx] == 0 or graph[ny][nx] != graph[y][x]:
                continue
            result += 1
            q.appendleft((ny, nx))
            visited[ny][nx] = True
    
    return result
            

if __name__ == "__main__":
    n = int(input())
    
    graph = []
    
    for _ in range(n):
        graph.append(list(map(int, input())))

    visited = [[False] * n for _ in range(n)]

    answer = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and graph[i][j] != 0:
                answer.append(bfs(graph, visited, i, j, n))

    answer.sort()
    print(len(answer))
    for i in answer:
        print(i)
