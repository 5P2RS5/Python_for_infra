def solution(s):
    answer = ''
    arr = list(s.split(' '))
    arr.sort(key=lambda x : int(x))

    answer = arr[0] + ' ' + arr[-1]
    print(answer)
    return answer

if __name__ == '__main__':
    solution("1 2 3 4")