# bfs

from collections import deque


def distance(x1, x2, y1, y2):
    return abs(y2 - y1) + abs(x2 - x1)
    

def bfs(y, x, visited, arr):
    q = deque()
    q.append((y, x))
    visited[0] = True 
    while q:
        py, px = q.popleft()

        if distance(arr[-1][0], py, arr[-1][1], px) <= 1000:
            print("happy")
            return
        
        for i in range(1, len(arr) - 1):
            if visited[i] == True :
                continue
            if distance(arr[i][0], py, arr[i][1], px) <= 1000:
                q.append((arr[i][0], arr[i][1]))
                visited[i] = True
    print("sad")

            



if __name__ == "__main__" :
    t = int(input())

    for _ in range(t):
        arr = []
        isCan = True
        c = int(input()) # 편의점 개수
        visited = [False] * (c+2)

        for _ in range(c + 2):
            arr.append(list(map(int, input().split())))
        
        bfs(arr[0][0], arr[0][1], visited, arr)