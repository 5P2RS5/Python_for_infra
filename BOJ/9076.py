T = int(input())

arr = [sorted(list(map(int, input().split()))) for _ in range(T)]

for i in arr:
    if i[3] - i[1] >= 4:
        print("KIN")
    else:
        print(i[3] + i[2] + i[1])
