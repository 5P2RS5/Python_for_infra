from collections import deque

def dfs(arr, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in arr[start]:
        if visited[i] == False:
            dfs(arr, i, visited)

def bfs(arr, start, visited):
    q = deque()
    visited[start] = True
    q.append(start)

    while q :
        f = q.popleft()
        print(f, end=" ")
        for i in arr[f]:
            if visited[i] == False :
                visited[i] = True
                q.append(i)



if __name__ == "__main__":
    n, m, v = map(int, input().split())
    l = [[] for _ in range(n + 1)] 
    for i in range(m):
        a, b = map(int, input().split())
        l[a].append(b)
        l[b].append(a)
    
    for i in l:
        i.sort()

    visited = [False] * (n + 1)
    dfs(l, v, visited)
        
    print()

    visited = [False] * (n + 1)
    bfs(l, v, visited)

