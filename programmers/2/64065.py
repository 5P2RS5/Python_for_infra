def solution(s):
    answer = []    
    arr = []
    temp = []
    result = ""
    for i in range(len(s)):
        if s[i].isnumeric():
            result += s[i]
        if s[i] == '}' and len(result) != 0:
            temp.append(int(result))
            result = ""
            arr.append(temp)
            temp = []
            continue
        if s[i] == ',' and len(result) != 0:
            temp.append(int(result))
            result = ""
    arr = sorted(arr, key = lambda x : len(x))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] not in answer:
                answer.append(arr[i][j])
    
    
    return answer