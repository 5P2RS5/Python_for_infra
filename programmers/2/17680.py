from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    q = deque()
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] in q :
            answer += 1
            q.remove(cities[i])
        else:
            answer += 5
            if len(q) >= cacheSize:
                q.popleft()
        q.append(cities[i])    
    
    return answer