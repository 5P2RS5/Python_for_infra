a, b, c = map(float, input().split())

sum = a * b * c / 8 / 1024 / 1024

print(format(sum, ".2f"), "MB")