# bfs

from collections import deque


def bfs(q, graph, n, m, h):

    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    while q:
        pz, py, px = q.popleft()
        for i in range(6):
            nz = pz + dz[i]
            ny = py + dy[i]
            nx = px + dx[i]
            if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n :
                if graph[nz][ny][nx] == 0:
                    q.append((nz, ny, nx))
                    graph[nz][ny][nx] = graph[pz][py][px] + 1


def find_max(graph, h, m, n):
    max_value = 0
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if graph[i][j][k] == 0:
                    return -1
                if max_value < graph[i][j][k]:
                    max_value = graph[i][j][k]
    
    return max_value - 1
    




if __name__ == "__main__":
    n, m, h = map(int, input().split())

    graph = []


    for i in range(h):
        graph.append([])
        for j in range(m):
            graph[i].append(list(map(int, input().split(' '))))

    q = deque()
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if graph[i][j][k] == 1:
                    q.append((i, j, k))
    bfs(q, graph, n, m, h)
    print(graph)
    print(find_max(graph, h, m, n))
        
