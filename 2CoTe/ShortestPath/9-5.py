import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def stra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
stra(c)
result = 0
cnt = 0
print(distance)
for i in distance:
    if(i != 0 and i < INF):
        cnt += 1
        result = max(i, result)

print(cnt, result)



