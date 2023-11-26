n = str(input())

l = sorted([int(i) for i in n], reverse=True)

for i in l:
    print(i, end='')