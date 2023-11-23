def solution(n, lost, reserve):
    answer = 0
    l = []
    for i in range(n):
        l.append(1)
    for i in reserve:
        l[i - 1] += 1
    for i in lost:
        l[i - 1] -= 1
    
    for i in range(0, n):
        if l[i] == 0:
            if (i == 0):
                if l[i + 1] == 2:
                    l[i + 1] -= 1
                    l[i] += 1
            elif(i == n - 1):
                if l[i - 1] == 2:
                    l[i - 1] -= 1
                    l[i] += 1
            else:
                if l[i - 1] == 2:
                    l[i - 1] -= 1
                    l[i] += 1
                elif l[i + 1] == 2:
                    l[i + 1] -= 1
                    l[i] += 1
    print(l)      
    for i in l:
        if(i > 0):
            answer += 1
    return answer