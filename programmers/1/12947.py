def solution(x):
    answer = False
    temp = sum(list(map(int, str(x))))
    if(x % temp == 0) : 
        return True
    return answer