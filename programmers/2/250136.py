from collections import deque


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    print(n, m)
    visited = [[False for _ in range(m)] for _ in range(n)]
    print(visited)
    return answer



if __name__=='__main__':
    solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])