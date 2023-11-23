# 큰 수의 법칙
a, b, c = map(int, input().split(' '))
l = list(map(int, input().split(' ')))

l.sort()

result = 0
for i in range(1, b + 1):
    if c % i : 
        result += l[-1]
    else:
        result += l[-2]

print(result)
