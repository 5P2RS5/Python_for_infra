# 피보나치 수열

# f(x) = f(x - 1) + f(x - 2)
# x == 1 or x == 2 => f(x) = 1 

def fibo(a):
    print("계산중")
    if a == 1 or a == 2:
        return 1
    return fibo(a - 1) + fibo(a - 2)

print(fibo(99))