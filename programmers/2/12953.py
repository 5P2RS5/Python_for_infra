def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

def gcd2(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd3(a, b):
    if(b == 0):
        return a
    else:
        gcd3(b, a % b)

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    answer = arr[0]
    for i in range(len(arr) - 1):
        if i == 0:
            answer = (answer * arr[i + 1]) // gcd(answer, arr[i + 1])
        else :
            answer = (answer * arr[i + 1]) // gcd(answer, arr[i + 1])
    return answer