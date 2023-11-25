from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    site = [[-1] * 102 for _ in range(102)]

    for i in rectangle:
        x1, y1, x2, y2 = map(lambda x : x * 2, i)
        for i in range(x1, x2 + 1):
            for j in range(y1, y1 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    site[i][j] = 0
                elif site[i][j] != 0:
                    site[i][j] = 1

    for i in range(15):
        for j in range(102):
            print(site[i][j], end=' ')
        print()

    return answer