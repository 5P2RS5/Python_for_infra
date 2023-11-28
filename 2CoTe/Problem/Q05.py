n, m = map(int, input().split())

arr = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i, n):
        if arr[i] != arr[j]:
            print("(",arr[i], arr[j],")")
            result += 1

print(result)