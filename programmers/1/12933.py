def solution(n):
    temp = map(str, sorted(list(map(int, str(n))), reverse=True))
    print(type(temp))
    answer = ''.join(temp)
    return int(answer)