n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    arr[i].append(0)

arr.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

arr[0][4] = 1
cnt = 1

for i in range(1, n):
    if(arr[i][1] == arr[i - 1][1] and arr[i][2] == arr[i - 1][2] and arr[i][3] == arr[i - 1][3]):
        arr[i][4] = arr[i - 1][4]
        cnt += 1
    else :
        arr[i][4] = arr[i - 1][4] + cnt
        cnt = 1
    

for i in range(n):
    if(arr[i][0] == k):
        print(arr[i][4])
    