
def solution(board, moves):
    answer = 0
    
    l = []
    c = []
    
    for i in range(0, len(board)):
        l.append([])
        for j in range(len(board) - 1, -1, -1):
            if(board[j][i] == 0):
                continue
            else:
                l[i].append(board[j][i])
    
    for i in moves:
        if len(l[i - 1]) >= 1 :
            top = l[i - 1].pop()
            c.append(top)
        if len(c) >= 2 and c[-1] == c[-2] :
            c.pop()
            c.pop()
            answer += 2
    
    return answer