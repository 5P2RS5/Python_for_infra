n = int(input())

arr = sorted(list(map(int, input().split())))

target = 1

for x in arr:
    if target < x :
        break
    target += x
        
print(target)