def solution(participant, completion):
    hashdict = {}
    temp = 0
    for i in participant:
        hashdict[hash(i)] = i
        temp += hash(i)

    for i in completion:
        temp -= hash(i)
    
    return hashdict[temp]