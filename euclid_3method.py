def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

def gcd2(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd3(a, b):
    if(b == 0):
        return a
    else:
        gcd3(b, a % b)