# dfs

def dfs(graph, visited, a, b, p):
    visited[a] = p

    for i in graph[a]:
        if i == b :
            visited[i] = p + 1
            return 
        if visited[i] == -1 :
            dfs(graph, visited, i, b, p + 1)
    return



if __name__ == "__main__":
    n = int(input())
    a, b = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [int(-1)] * (n + 1)
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    dfs(graph, visited, a, b, 1)
    if visited[b] == -1:
        print(-1)
    else:
        print(visited[b] - 1)
