def solution(nums):
    answer = 0
    arr = set()
    for i in range(len(nums)):
        arr.add(nums[i])
        
    size = len(nums) // 2
    size2 = len(arr)
    
    if size < size2 :
        answer = size
    else:
        answer = size2
    
    return answer