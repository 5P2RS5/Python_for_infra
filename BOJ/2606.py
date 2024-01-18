# dfs

def dfs(graph, visited, n):
    visited[n] = True
    
    for i in graph[n]:
        if visited[i] == False:
            dfs(graph, visited, i)
    
    return

if __name__ == "__main__":
    n = int(input())
    cnt = int(input())
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(cnt):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    dfs(graph, visited, 1)

    print(visited.count(True) - 1)


