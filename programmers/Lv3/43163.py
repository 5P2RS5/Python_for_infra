from collections import deque


def solution(begin, target, words):
    answer = 0
    
    if not target in words : 
        return 0
    
    q = [begin]
    
    while True:
        print(q)
        temp = []
        for word in q:
            if word == target:
                return answer
            
            for i in range(len(words) - 1, -1, -1):
                word_test = words[i]
                hap = 0
                for a, b in zip(word, word_test):
                    if str(a) != str(b):
                        hap += 1
                if(hap == 1):
                    temp.append(words.pop(i))
        if not temp:
            return 0
        q = temp
        answer += 1
        
    return answer
