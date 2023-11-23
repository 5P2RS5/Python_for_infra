from collections import deque



def dfs(y, x, computers, visited, n):
    for i in range(x, n):
        if(visited[i] or computers[y][i] == 0):
            continue
        visited[i] = True
        dfs(i, 0, computers, visited, n)
        
        
        
        

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(0, n):
        for j in range(0, n):
            if(visited[i] == False and computers[i][j] == 1):
                dfs(i, j, computers, visited, n)
                answer += 1
    for i in range(n):
            print(visited[i], end=' ')
            
    return answer