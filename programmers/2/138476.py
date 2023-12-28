from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    dic = defaultdict(int)
    
    for i in range(len(tangerine)):
        dic[tangerine[i]] += 1
    
    dic = sorted(dic.items(), key = lambda x : x[1], reverse=True)
    
    for i in range(len(dic)):
        k -= dic[i][1]
        answer += 1
        if k <= 0:
            break

    return answer