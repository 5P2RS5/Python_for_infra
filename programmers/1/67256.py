import math
def solution(numbers, hand):
    answer = ''
    
    pad = [[1,2,3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    l = [3, 0]
    r = [3, 2]
    
    for i in numbers :
        if i == 1 or i == 4 or i == 7 : 
            answer += 'L'
            if(i == 1):
                l = [0, 0]
            if(i == 4):
                l = [1, 0]
            if(i == 7):
                l = [2, 0]
            
        elif i == 3 or i == 6 or i == 9: 
            answer += 'R'
            if(i == 3):
                r = [0, 2]
            if(i == 6):
                r = [1, 2]
            if(i == 9):
                r = [2, 2]
            print("l", l)
            
        else :
            c = [0, 0]
            if i == 2 :
                c = [0, 1]
            if i == 5 :
                c = [1, 1]
            if i == 8 :
                c = [2, 1]
            if i == 0 :
                c = [3, 1]
            
            a = abs(l[0] - c[0]) + abs(l[1] - c[1])
            b = abs(r[0] - c[0]) + abs(r[1] - c[1])
            if a == b:
                if hand == "right" : 
                    answer += 'R'
                    r = c
                else :
                    answer += 'L'
                    l = c
            elif a < b:
                answer += 'L'
                l = c
            elif a > b:
                answer += 'R'
                r = c
        
    return answer