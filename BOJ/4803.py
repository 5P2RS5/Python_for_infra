import sys
sys.setrecursionlimit(10**3)


def dfs(graph, s):
    global visited
    global flag
    visited[s] = True
    for i in graph[s]:
        if i == s:
            continue
        if visited[i]:
            return False
        if not dfs(s, i):
            return False
        return True




if __name__ == "__main__":
    T = 1
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            exit()
        graph = [[] for i in range(n + 1)]
        result = 0
        global visited
        global flag
        visited = [False for i in range(n + 1)]
        for i in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)

        for i in range(n):
            graph[i].sort()
        #print(graph)            
        for i in range(1, n + 1):
            flag = True
            if len(graph[i]) == 0:
                continue
            if visited[i] == True:
                continue
            dfs(graph, i)
            if flag : 
                result += 1
        result += visited.count(False) - 1
        if result > 1:
            print("Case %d: A forest of %d trees." % (T, result))
        elif result == 1:
            print("Case %d: There is one tree." %T)
        else:
            print("Case %d: No trees." %T)

            
        


