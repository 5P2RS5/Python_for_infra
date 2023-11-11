x, y = map(int, input().split())

print(bool((x and (not y)) or ((not x) and y)))