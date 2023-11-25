a = [1, 2, 3, 4, 5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    
    scores = [0, 0, 0]
    
    for idx, ch in enumerate(answers):
        if a[idx % len(a)] == ch :
            scores[0] += 1
        if b[idx % len(b)] == ch :
            scores[1] += 1
        if c[idx % len(c)] == ch :
            scores[2] += 1
            
    v = max(scores)
      
    for idx, score in enumerate(scores) :
        if score == v:
            answer.append(idx + 1)
    
    answer.sort()
    return answer