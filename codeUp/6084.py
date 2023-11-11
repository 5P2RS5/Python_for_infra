a, b, c, d = map(float, input().split())

sum = a * b * c * d / 8 / 1024 / 1024

print(format(sum, ".1f"), "MB")