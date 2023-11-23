# 반복문

l = [1,3,5,7,9,11,13,15,17,19,21]

target = int(input())

start = 0
end = len(l) - 1

while start <= end:
    mid = (start + end) // 2
    
    if(l[mid] == target):
        print(mid + 1)
        break
    elif(l[mid] < target):
        start = mid + 1
    else:
        end = mid - 1
    
print(-1)
