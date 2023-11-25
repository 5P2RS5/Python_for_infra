def bst(start, end, arr, target) :
    if start > end :
        return False
    mid = (end + start) // 2
    if arr[mid] == target :
        return True
    elif arr[mid] < target :
        return bst(mid + 1, end, arr, target)
    else :
        return bst(start, mid - 1, arr, target)



n = int(input())

l = sorted(list(map(int, input().split())))

m = int(input())

chk = list(map(int, input().split()))

for item in chk:
    if bst(0, n - 1, l, item):
        print("yes", end=' ')
    else:
        print("no", end=' ')



