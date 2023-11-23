dy = [-1, 1, -2, -2, -1, 1, 2, 2]
dx = [-2, -2, -1, 1, 2, 2, 1, -1]

pos = input()

x = int(ord(pos[0]) - ord('a'))
y = int(pos[1]) - 1
answer = 0

for i in range(8):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny < 0 or nx < 0 or nx >= 7 and ny >= 7 :
        continue
    answer += 1

print(answer)