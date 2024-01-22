
max_value = 0



n = int(input())

graph = [[]]
dist = [[0 for _ in range(n + 1)] for i in range(n + 1)]

def dfs(node, weight):
    for idx, w in enumerate(dist[node]):
        if length[idx] == -1:
            length[idx] = weight + w
            dfs(idx, weight + w)



for i in range(1, n + 1):
    graph.append(list(map(int, input().split())))
print(graph)


for i in range(1, n + 1):
    for j in range(1, len(graph[i]) - 1, 2):
        dist[i][graph[i][j]] = graph[i][j + 1]
        dist[graph[i][j]][i] = graph[i][j + 1]

length = [-1] * (n + 1)
dfs(1, 0)
print(length)

start = length.index(max(length))
length = [-1] * (n + 1)
print(start)
print(length)
length[start] = 0
dfs(start, 0)

    
print(max(length))

