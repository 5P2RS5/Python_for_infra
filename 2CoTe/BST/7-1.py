# 순차 탐색

def sequential_search(n, target, array):
    for i in range(n):
        if(array[i] == target):
            return i
        

who = str(input())

names = list(map(str, input().split()))

pos = sequential_search(len(names), who, names)
print(pos + 1, names[pos])