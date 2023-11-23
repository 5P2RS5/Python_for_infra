a, b = map(int, input().split())

answer = 0
while a != 1 :
    if not a % b:
        a /= b
    else :
        a -= 1
    answer += 1
print(answer)