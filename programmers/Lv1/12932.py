def solution(n):
    temp = str(n)
    answer = []
    for i in range(len(temp) - 1, -1, -1):
        answer.append(int(temp[i]))
    print(answer)
    return answer