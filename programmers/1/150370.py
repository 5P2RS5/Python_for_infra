def solution(today, terms, privacies):
    
    answer = []
    todate = list(map(int, today.split('.')))
    day = 28 * 12 * todate[0] + 28 * (todate[1] - 1) + todate[2]
    dic = {}
    for i in terms :
        a, b = list(map(str, i.split(' ')))
        dic[a] = int(b)
    for i in range(len(privacies)):
        s = list(map(str, privacies[i].split(' ')))
        t = list(map(int, s[0].split('.')))
        
        hap = dic[s[1]] * 28
        print(hap)
        temp = 28 * 12 * t[0] + 28 * (t[1] - 1) + t[2] + hap
        
        print("day", day)
        print("temp", temp)
        if(day >= temp):
            answer.append(i + 1)
    return answer