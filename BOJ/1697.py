# bfs

from collections import deque

def bfs(graph, v, target, max):
    q = deque()
    q.append(v)

    while q:
        top = q.popleft()
        if top == target:
            return 
        for next_v in (top * 2, top - 1, top + 1):
            if top == next_v:
                continue
            if next_v < 0 or next_v > max:
                continue
            if graph[next_v] != 0:
                continue
            q.append(next_v)
            graph[next_v] = graph[top] + 1


if __name__ == "__main__":
    INF = int(100001)
    
    a, b = map(int, input().split())

    graph = [int(0)] * (INF + 1)

    bfs(graph, a, b, INF)
    print(graph[b])

