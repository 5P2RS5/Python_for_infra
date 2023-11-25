def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    else:
        min = arr[0]
        for i in arr:
            if(i < min):
                min = i
        arr.remove(min)

    return arr