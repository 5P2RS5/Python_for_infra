def dfs(s, cnt, tickets, visited, answer):
    global isOk
    answer.append(s)
    if(cnt == len(tickets)):
        isOk = True
    
    for i in range(len(tickets)):
        if(visited[i]) : 
            continue
        if(tickets[i][0] == s):
            visited[i] = True
            dfs(tickets[i][1], cnt + 1, tickets, visited, answer)

            if not isOk:
                answer.pop()
                visited[i] = False    
    print(answer)



def solution(tickets):
    answer = []
    global isOk
    tickets.sort()
    isOk = False
    visited = [False] * len(tickets)
    dfs("ICN", 0, tickets, visited, answer)
    return answer