n = int(input())

arr = [[] for _ in range(100001)]

for _ in range(n):
    pos, color = map(int, input().split())
    arr[color].append(pos)

for i in range(100001):
    arr[i].sort()

result = 0
for i in range(100001):
    if len(arr[i]) == 0 or len(arr[i]) == 1:
        continue
    if len(arr[i]) :
        for j in range(len(arr[i])):
            if j == 0:
                result += arr[i][j + 1] - arr[i][j]
            elif j == len(arr[i]) - 1:
                result += arr[i][j] - arr[i][j - 1]
            else:
                result += min(arr[i][j + 1] - arr[i][j], arr[i][j] - arr[i][j - 1])    

print(result)