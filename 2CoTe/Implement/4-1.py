dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

n = int(input())
l = list(map(str, input().split(' ')))

s = [1, 1] #y, x

for i in l:
    if i == 'R' and s[1] != n:
        s[0] += dy[0]
        s[1] += dx[0]
    if i == 'L' and s[1] != 1:
        s[0] += dy[1]
        s[1] += dx[1]
    if i == 'U' and s[0] != 1:
        s[0] += dy[2]
        s[1] += dx[2]
    if i == 'D' and s[0] != n:
        s[0] += dy[3]
        s[1] += dx[3]
    print(s)
        
print(s)