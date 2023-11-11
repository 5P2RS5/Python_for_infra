a, b, c, d = map(int, input().split())

sum = a

for i in range (1, d) : 
    sum = sum * b + c

print(sum)
