import math

def solution(n):
    temp = math.ceil(math.sqrt(n)) # math.ceil : 소수점 존재시 정수 + 1
    answer = -1
    if(math.pow(temp, 2) == n):
        answer = math.pow(temp + 1, 2)
    return int(answer)

print(solution(101))