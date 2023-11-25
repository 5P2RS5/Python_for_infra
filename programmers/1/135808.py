from itertools import combinations

def solution(k, m, score):
    score.sort()
    answer = 0
    for i in range(len(score) - m, -1, -m):
        answer += m * score[i]
    return answer