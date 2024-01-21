# bfs

from collections import deque

def bfs(n, graph, y, x, v, visited):

    q = deque()
    q.append((y, x))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        py, px = q.popleft()

        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            
            if ny >= n or nx >= n or ny < 0 or nx < 0:
                continue
            if visited[ny][nx] == True or graph[ny][nx] <= v:
                continue
            visited[ny][nx] = True
            q.append((ny, nx))


    




if __name__ == "__main__":
    n = int(input())

    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split(' '))))
    


    v = 0
    answer = 0
    while True:
        cnt = 0
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if visited[i][j] == False and graph[i][j] > v:
                    bfs(n, graph, i, j, v, visited)
                    cnt += 1

        if cnt == 0:
            break

        if answer < cnt:
            answer = cnt
        v += 1
        
    print(answer)
    
    
    