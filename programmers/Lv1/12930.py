def solution(s):
    a = s.split(' ')
    answer = ''
    
    for i in range(0, len(a)):
        temp = ''
        for j in range(0, len(a[i])):
            if(j % 2 == 0):
                temp += a[i][j].upper()
            else:
                temp += a[i][j].lower()  
        answer += temp + " "
    
    return answer[0:-1]