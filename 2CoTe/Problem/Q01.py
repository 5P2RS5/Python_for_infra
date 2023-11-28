n = int(input())

arr = sorted(list(map(int, input().split())))

cnt = 0
answer = 0
for i in range(len(arr)):
    val = arr[i]
    cnt += 1
    if cnt == arr[i]:
        print(i, cnt)
        answer += 1
        cnt = 0

print(answer)