import time
start = time.time()  # 시작 시간 저장

def bst(target, array, start, end):
    if(start > end):
        print(start, end)
        return -1
    mid = (start + end) // 2
    if(array[mid] == target):
        return mid
    elif(array[mid] > target):
        print(start, mid - 1, target)
        return bst(target, array, start, mid - 1)
    else:
        print(mid + 1, end, target)
        return bst(target, array, mid + 1, end)

N = [5,1,4,2,9]

l = [1, 4, 3]

# for i in l:
#     if i in N:
#         print("yes")
#     else:
#         print("No")

for i in l:
    bst(i, N, 0, len(N) - 1)

 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간