import functools

def comp(a, b):
    if int(a + b) > int(b + a):
        return 1
    elif int(a + b) < int(b + a):
        return -1
    return 0

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = functools.cmp_to_key(comp), reverse = True)
    answer = int(''.join(map(str,numbers)))
    return str(answer)


######## 다른 사람 풀이

def other(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer

print(other([6, 10, 2]))