d = [0] * 100

def fibo(a):
    if a == 1 or a == 2:
        return 1
    if d[a] == 0:
        d[a] = fibo(a - 1) + fibo(a - 2)
    else:
        return d[a]
    return d[a]
        

if __name__=="__main__":
    print(fibo(99))