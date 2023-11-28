zero = 0
one = 0

n = str(input())

i = 0
s = n[i]
while i < len(n) - 1:
    if s != n[i + 1]:
        if n[i] == '1':
            one += 1
        else:
            zero += 1
        s = n[i + 1]
    i += 1

if n[i] == '1':
    one += 1
else:
    zero += 1

print(min(zero, one))