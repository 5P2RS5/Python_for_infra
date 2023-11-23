from collections import deque

def bfs(graph, v, visited):
    visited[v] = True
    q = deque()
    q.append(v)
    while len(q) != 0 :
        top = q.popleft()
        print(top, end=' ')
        for i in graph[top]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [[],
         [2, 3, 8], [1,7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9

bfs(graph, 1, visited)
