def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    n = [] 
    m = []
    arr = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            n.append(str1[i] + str1[i + 1])
            
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            m.append(str2[i] + str2[i + 1])
            
    n = sorted(n)
    m = sorted(m)
    print(n)
    print(m)
    arr2 = []
    if len(n) >= len(m):
        arr2 = n.copy()
        for i in range(len(m)):
            if m[i] in n:
                idx = n.index(m[i])
                arr.append(m[i])
                n[idx] = "**"
            else:
                arr2.append(m[i])
    else:
        arr2 = m.copy()
        for i in range(len(n)):
            if n[i] in m:
                idx = m.index(n[i])
                arr.append(n[i])
                m[idx] = "**"
            else:
                arr2.append(m[i])
    print(n)
    print(m)
    print(arr)
    print(arr2)
    a = 0
    b = 0
    if len(arr2) == 0:
        b = 1
    else:
        b = len(arr2)
        
    if len(arr) == 0 and len(arr2) == 0:
        a = 1
    else:
        a = len(arr)
    
        
    answer = int(a / b * 65536)
            
    return answer