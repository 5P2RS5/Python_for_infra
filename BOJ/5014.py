# bfs
from collections import deque

if __name__ == "__main__":
    f, s, g, u, d = map(int, input().split())

    inf = 1000001
    visited = [int(0)] * inf

    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        top = q.popleft()
        if top == g:
            break
        for next_s in (top + u, top - d):
            if next_s <= 0 or next_s > f:
                continue
            if visited[next_s] != 0:
                continue
            q.append(next_s)
            visited[next_s] = visited[top] + 1
    if visited[g] != 0:
        print(visited[g] - 1)
    else:
        print("use the stairs")
    

        