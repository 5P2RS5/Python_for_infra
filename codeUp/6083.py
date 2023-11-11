x, y, z = map(int, input().split())

sum = int(0)
for i in range (0, x) :
    for j in range(0, y) :
        for k in range(0, z) :
            print(i, j, k)
            sum += 1

print(sum)