n, m = map(int, input().split())

l = list(map(int, input().split()))

end = max(l)
start = 0

result = 0

while start <= end :
    total = 0
    mid = (start + end) // 2

    for x in l:
        if x > mid :
            total += x - mid
    
    if total < m :
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
    