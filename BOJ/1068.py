#dfs

def dfs(graph, s, k):
    global visited
    global result
    if visited[s] == True or s == k:
        return
    visited[s] = True
    if len(graph[s]) == 0 or (len(graph[s]) == 1 and graph[s][0] == k):
        result += 1
    for i in graph[s]:
        if visited[i] == True or i == k:
            continue
        dfs(graph, i, k)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    root = arr.index(-1)
    if k == root :
        print(0)
        exit()
    global visited
    global result
    result = 0
    visited = [False for _ in range(n)]
    
    graph = [[] for _ in range(n)]
    for i in range(n):
        if arr[i] == -1:
            continue
        graph[arr[i]].append(i)

    dfs(graph, root, k)
    print(result)
    
