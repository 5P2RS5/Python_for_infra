#bfs

from collections import deque

def bfs(y, x, d, graph, n, m):
    q = deque()
    q.append((y, x))
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    result = 0
    while q : 
        py, px = q.popleft()
        # 현재 칸 청소 안되면 청소
        if graph[py][px] == 0:
            graph[py][px] = 2
            result += 1


            
        # #print("dir : ", d)
        # #print("resilt : ", result)
        # for i in range(n):
        #     for j in range(m):
        #         print(graph[i][j], end = ' ')
        #     print()
        # print(result)




        # 현재 칸 주변에 빈칸이 있는가?
        space = 0
        for i in range(4):
            #print((d + i) % 4)
            ny = py + dy[i]
            nx = px + dx[i]
            if graph[ny][nx] == 0:
                space += 1

        if space == 0:
            ny = py + dy[(d + 2) % 4]
            nx = px + dx[(d + 2) % 4]
            if graph[ny][nx] == 1:
                return result
            # 후진
            else:
                q.append((ny, nx))
        else:
            for i in range(4):
                d -= 1
                if d == -1:
                    d = 3
                ny = py + dy[d]
                nx = px + dx[d]
                if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                    q.append((ny, nx))
                    break
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    y, x, d = map(int, input().split())

    graph = []
    
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    print(bfs(y, x, d, graph, n, m))
