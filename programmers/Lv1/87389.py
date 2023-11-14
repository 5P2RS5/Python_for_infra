def solution(n):
    return [answer for answer in range(1, n + 1) if n % answer == 1][0]