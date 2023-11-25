def solution(N, stages):
    answer = []
    dic = {}
    for i in range(N + 1) :
        dic[str(i + 1)] = 0
    
    for j in stages:
        dic[str(j)] += 1
    
    cnt = len(stages)
    i = 1
    while cnt > 0 :
        temp = dic[str(i)]
        dic[str(i)] = dic[str(i)] / cnt
        cnt -= temp
        i += 1
        
    dic[str(N + 1)] = 0
    
    dic = sorted(dic.items(), reverse=True, key=lambda x:x[1])
    for i in range(0, N) :
        answer.append(int(dic[i][0]))
    return answer