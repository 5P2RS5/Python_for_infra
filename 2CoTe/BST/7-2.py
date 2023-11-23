# 재귀함수

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

l = [8,7,3,2,0,4,1,9,6,5]


target = int(input())

l.sort()
print(l)
answer = bst(target, l, 0, len(l) - 1)

print(answer)