def solution(n, arr1, arr2):
    answer = []
    for j, k in zip(arr1, arr2):
        s = str(bin(j|k)[2:])
        s = s.rjust(n, '0')
        s = s.replace('1', '#')
        s = s.replace('0', ' ')
        answer.append(s)
        
    return answer