import sys
sys.setrecursionlimit(10**5)
# dfs

def dfs(start, graph, visited):
    for i in graph[start]:
        if visited[i] != -1:
            continue
        visited[i] = visited[start] + 1
        dfs(i, graph, visited)




if __name__ == "__main__":
    n, m, r = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [-1 for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n):
        graph[i].sort()

    visited[r] = 0
    dfs(r, graph, visited)
    for i in range(1, n + 1):
        print(visited[i])
    
