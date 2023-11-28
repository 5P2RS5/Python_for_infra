from collections import deque

def solution(food_times, k):
    answer = 0
    arr = deque()
    for idx, item in enumerate(food_times):
        arr.append((idx, item))


    while k > 1:
        if arr[0][1] != 0:
            idx, time = arr[0]
            arr.popleft()
            arr.append((idx, time - 1))
        k -= 1
    
    print(arr)
    if arr[0][1] == 0:
        return -1
    return arr[0][0]

print(solution([3, 1, 2], 5))