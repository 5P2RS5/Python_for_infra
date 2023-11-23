answer = 0
def dfs(v, arr, target, size, temp):
    global answer
    if(len(temp) == size):
        if sum(temp) == target : 
            answer += 1
        return
    temp.append(arr[v])
    dfs(v + 1, arr, target, size, temp)
    temp.pop()
    temp.append(arr[v] * -1)
    dfs(v + 1, arr, target, size, temp)
    temp.pop()

def solution(numbers, target):
    temp = []
    global answer
    dfs(0, numbers, target, len(numbers), temp)
    return answer

