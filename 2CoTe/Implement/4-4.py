

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

n, m = map(int, input().split())

y, x, dir = map(int, input().split())

l = []


for i in range(n):
    temp = list(map(int, input().split()))
    l.append(temp)

answer = 1
l[y][x] = 1

while True:
    finding = False
    for i in range(4):
        ny = y + dy[(i + 1) % 4]
        nx = x + dx[(i + 1) % 4]
        
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue

        if l[ny][nx] == 1:
            continue

        dir += 1
        y, x = ny, nx
        answer += 1
        l[ny][nx] = 1
        finding = True
        print(y, x)
        break

    if not finding : 
        y += dy[dir] * -1
        x += dx[dir] * -1
        if l[y][x] == 1:
            break


print(answer)
print(l)