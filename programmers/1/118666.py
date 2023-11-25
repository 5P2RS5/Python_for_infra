def solution(survey, choices):
    answer = ''
    dic = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for idx, value in enumerate(choices):
        value -= 4
        if value < 0 :
            dic[survey[idx][0]] += (-1 * value)
        else:
            dic[survey[idx][1]] += value
    print(dic)
    if(dic['R'] >= dic['T']):
        answer += 'R'
    else:
        answer += 'T'
        
    if(dic['C'] >= dic['F']):
        answer += 'C'
    else:
        answer += 'F'
    
    if(dic['J'] >= dic['M']):
        answer += 'J'
    else:
        answer += 'M'
        
    if(dic['A'] >= dic['N']):
        answer += 'A'
    else:
        answer += 'N'
    return answer