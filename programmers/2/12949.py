def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): 
        answer.append([])
        for j in range(len(arr2[0])):
            result = 0
            for k in range(len(arr1[0])):
                result += arr1[i][k] * arr2[k][j]
            answer[i].append(result)
    return answer