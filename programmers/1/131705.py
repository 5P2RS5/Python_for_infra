from itertools import combinations

def solution(number):
    answer = 0
    answer = sum(1 for x in combinations(number, 3) if sum(x) == 0)
    return answer