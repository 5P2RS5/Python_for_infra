n = int(input())

N = 2 ** n - 1

def hanoi(k, a, b, c):
    if k == 1 :
        print(a, c)
        return
    
    hanoi(k - 1, a, c, b)
    print(a, c)
    hanoi(k - 1, b, a, c)

print(N)

if(n <= 20):
    hanoi(n, 1, 2, 3)