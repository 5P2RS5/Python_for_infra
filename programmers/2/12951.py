def solution(s):
    answer = ''
    arr = list(s)
    pos = 0
    while True:
        if arr[pos] != " ":
            break
        answer += arr[pos]
        pos += 1
    isFirst = True

    for i in range(pos, len(arr)):
        if arr[i].isdigit():
            isFirst = False
        if arr[i].isupper() and not isFirst:
            arr[i] = arr[i].lower()
        if arr[i].isalpha() and isFirst:
            arr[i] = arr[i].upper()
            isFirst = False
        if arr[i] == " ":
            isFirst = True
        answer += arr[i]
    return answer

print(solution("  for the what 1what  "))