x, y, z = map(int, input().split())

k = x if(x < y) else y


print(k if(k < z) else z)
