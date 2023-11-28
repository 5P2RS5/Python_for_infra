n = int(input())

for _ in range(n):
    arr = []
    ps = list(str(input()))
    for i in range(len(ps)):
        if ps[i] == '(' :
            arr.append('(')
        else:
            if arr and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(')')
    if arr :
        print("NO")
    else:
        print("YES")               

