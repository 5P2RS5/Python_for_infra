p = []

for i in range(10):
    p.append(list(map(int, input().split())))

x = 1  
y = 1

while True:
    if (p[x][y] == 0):
        p[x][y] = 9
    elif (p[x][y] == 2):
        p[x][y] = 9
        break

    if (x==8 and y==8) or (p[x][y+1] == 1 and p[x+1][y] == 1):
        break

    if p[x][y+1] != 1 : 
        y += 1
    elif p[x+1][y] != 1 :
        x += 1

for i in range(10):
    for j in range(10):
        print(p[i][j], end=' ')
    print()