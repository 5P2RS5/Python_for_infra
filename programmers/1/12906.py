def solution(arr):
    answer = []
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i - 1])
    answer.append(arr[len(arr) - 1])
    return answer