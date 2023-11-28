
n = int(input())

arr = []
for _ in range(n):
    a = int(input())
    if a == 0 and arr : 
        arr.pop()
    else:
        arr.append(a)
    
print(sum(arr))