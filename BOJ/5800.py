t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    arr2 = sorted(arr[1:])
    gap = 0
    for j in range(len(arr2) - 1):
        if gap < arr2[j + 1] - arr2[j]:
            gap = arr2[j + 1] - arr2[j]

    print("Class", i + 1)
    print("Max ", arr2[-1], ", Min ", arr2[0],", Largest gap ", gap, sep='')
    