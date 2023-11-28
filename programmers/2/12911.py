def numCnt(n):
    b = str((bin(n)[2:]))
    one = b.count('1')
    return one




def solution(n):
    answer = 0
    info_n = numCnt(n)
    n += 1
    while True:
        k = numCnt(n)
        if k == info_n:
            answer = n
            break
        n += 1
    return answer




if __name__ == '__main__':  
   print(solution(78))