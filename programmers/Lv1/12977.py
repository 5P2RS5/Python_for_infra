from itertools import combinations

def eratos(nums):
    a = [False, False] + (50 * 1000 - 1) * [True]
    prime = []
    for i in range(2, 50 * 1000 + 1):
        if a[i] == True:
            prime.append(i)
            #print(prime)
            for j in range(i * 2, 50 * 1000 + 1, i):
                a[j] = False
    return prime

def solution(nums):
    answer = 0
    primes = eratos(50 * 1000)
    temp = list(combinations(nums, 3))
    #print(primes)
    #print(temp)
    for i in temp:
        if sum(i) in primes :
            answer += 1


    return answer