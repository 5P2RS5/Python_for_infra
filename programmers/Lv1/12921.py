
# 에라토스테네스의 체
def solution(n):
    answer = 0
    
    arr = [False, False] + [True] * (n - 1)
    primes = []
    
    for i in range(2, n + 1):
        if arr[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                arr[j] = False
    
    answer = len(primes)
    
    return answer