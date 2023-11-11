n, m = map(int, input().split())

arr = []

for i in range(n) : 
    arr.append([])
    for j in range(m) :
        arr[i].append(int(0))

size = int(input())

for i in range(0, size) : 
    l, d, x, y = map(int, input().split())
    if(d == 1) : 
        for j in range(0, l) :
            arr[x + j - 1][y - 1] = 1
           
    if(d == 0) : 
        for k in range(0, l) :
            arr[x - 1][y + k - 1] = 1
    
        
for a in range(n) :
    for b in range(m) : 
        print(arr[a][b], end=' ')
    print()
