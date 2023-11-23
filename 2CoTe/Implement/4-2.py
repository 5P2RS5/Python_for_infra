n = int(input())

max = [n, 59, 59]

s = [0, 0, 0]

answer = 0
while answer < 11475:
    if(max[0] == s[0] and max[1] == s[1] and max[2] == s[2]) : 
        break
    
    temp = "".join(map(str, s))
    if str(n) in temp :
        answer += 1
    s[2] += 1
    if s[2] == 60:
        s[2] = 0
        s[1] += 1
    if s[1] == 60:
        s[0] += 1
        s[1] = 0

print(answer + 1)