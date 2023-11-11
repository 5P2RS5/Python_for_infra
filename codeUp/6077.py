x = int(input())


i = 0

sum = 0
for i in range(0, x + 1) :
    if(i % 2 == 0):
        sum += i

print(sum)