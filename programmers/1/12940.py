import math

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    

def solution(n, m):
    answer = []
    answer.append(gcd(max(n, m), min(n, m)))
    answer.append(n * m // answer[0])
    print(answer)
    return answer
