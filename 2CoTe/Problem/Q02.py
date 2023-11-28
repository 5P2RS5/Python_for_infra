
n = list(map(int, input().strip('0')))

result = n[0]
for i in range(1, len(n)):
    if n[i] <= 1:
        result += n[i]
    else:
        result *= n[i]

print(result)