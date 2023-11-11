n = int(input())

for i in range(n) : 
    x, y = map(int, input().split())
    for j in range(1, 20):
        if arr[j][int(y)] == 0:
            arr[j][int(y)] = 1
        else:
            arr[j][int(y)] = 0

        if arr[int(x)][j] == 0:
            arr[int(x)][j] = 1
        else:
            arr[int(x)][j] = 0