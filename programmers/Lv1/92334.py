def solution(id_list, report, k):
    answer = []
    ing = {}
    ed = {}
    for i in id_list:
        ing[i] = []
        ed[i] = 0
    
    for i in report:
        l = list(i.split(' '))
        if l[1] not in ing[l[0]]:
            ed[l[1]] += 1
            ing[l[0]].append(l[1])

    for i in id_list : 
        temp = 0
        for j in ing[i] :
            if(ed[j] >= k):
                temp += 1
        answer.append(temp)
    
    return answer